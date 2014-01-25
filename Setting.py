def getKsCreInfo():
    info = {}
    info['username'] = 'admin'
    info['password'] = 'password'
    info['tenant_name'] = 'demo'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0'
    return info

def getNovaCreInfo():
    info = {}
    info['username'] = 'admin'
    info['api_key'] = 'password'
    info['auth_url'] = 'http://10.0.2.15:5000/v2.0/'
    info['project_id'] = 'demo'
    return info
