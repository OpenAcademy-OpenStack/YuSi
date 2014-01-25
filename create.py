import keystoneclient.v2_0.client as ksclient 
import glanceclient as gcclient
import novaclient.v1_1.client as nvclient

from Setting import getKsCreInfo, getNovaCreInfo

def create():
    ksCreInfo = getKsCreInfo()
    novaCreInfo = getNovaCreInfo()
    keystoneCli = ksclient.Client(**ksCreInfo)
    novaCli = nvclient.Client(**novaCreInfo)
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
    print "starting spawn new instance......"
    print "new instance name : %s " % instance.name
    print "new instance id : %s " % instance.id
    print 'using "nova list" to check status'

if __name__ == '__main__':
    create()
