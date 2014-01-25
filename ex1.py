import keystoneclient.v2_0.client as ksclient 
import glanceclient as gcclient
import novaclient.v1_1.client as nvclient

def getCredentialInfo():
    info = {}
    info['username'] = 'admin'
    info['password'] = 'password'
    info['tenant_name'] = 'demo'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0'
    return info

def getNovaCredentialInfo():
    info = {}
    info['username'] = 'admin'
    info['api_key'] = 'password'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    info['project_id'] = 'demo'
    return info

if __name__ == '__main__':
    credentialInfo = getCredentialInfo()
    novaCreInfo = getNovaCredentialInfo()
    keystoneCli = ksclient.Client(**credentialInfo)
    novaCli = nvclient.Client(**novaCreInfo)
    #print keystoneCli.tenants.list()
    gcEndpoint = keystoneCli.service_catalog.get_urls(service_type='image')[0]
    glanceCli = gcclient.Client('1', gcEndpoint, token=keystoneCli.auth_token)
    
    images = glanceCli.images.list()
    image_create = None
    for image in images:
        if not image.name.find('ubuntu') == -1:
             image_create = image
             break
            
    flavor = novaCli.flavors.find(name='m1.micro')
    instance = novaCli.servers.create(name="test", image=image_create, flavor=flavor)
    print "waiting for instance to build"
#    while instance.status == 'BUILD':
#        instance = novaCli.servers.get(instance.id)
    print instance.status

    
            
    
