import keystoneclient.v2_0.client as ksclient 
import glanceclient as gcclient

def getCredentialInfo():
    info = {}
    info['username'] = 'admin'
    info['password'] = 'password'
    info['tenant_name'] = 'demo'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0'
    return info

if __name__ == '__main__':
    credentialInfo = getCredentialInfo()
    keystoneCli = ksclient.Client(**credentialInfo)
    #print keystoneCli.tenants.list()
    gcEndpoint = keystoneCli.service_catalog.get_urls(service_type='image')[0]
    glanceCli = gcclient.Client('1', gcEndpoint, token=keystoneCli.auth_token)
    images = glanceCli.images.list()
    for image in images:
        if not image.name.find('ubuntu') == -1:
            print image
            
    
