import os

os.environ['http_proxy'] = 'http://web-proxy.atl.hp.com:8080'
os.environ['HTTP_PROXY'] = 'http://web-proxy.atl.hp.com:8080'
os.environ['https_proxy'] = 'http://web-proxy.atl.hp.com:8080'
os.environ['HTTPS_PROXY'] = 'http://web-proxy.atl.hp.com:8080'
os.environ['no_proxy'] = 'localhost,127.0.0.1/8'
print('http:   ' + os.environ['http_proxy'])
print('HTTP:   ' + os.environ['HTTP_PROXY'])
print('https:  ' + os.environ['https_proxy'])
print('HTTPS:  ' + os.environ['HTTPS_PROXY'])
print('NO:     ' + os.environ['no_proxy'])