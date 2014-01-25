from keystoneclient.v2_0 import client

def getCredentialInfo():
    info = {}
    info['username'] = 'admin'
    info['password'] = 'password'
    info['tenant_name'] = 'demo'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0'
    return info

if __name__ == '__main__':
    credentialInfo = getCredentialInfo()
    keystoneCli = client.Client(**credentialInfo)
    print keystoneCli.tenants.list()
