import os

if 'http_proxy' in os.environ:
    del os.environ['http_proxy']

if 'HTTP_PROXY' in os.environ:
    del os.environ['HTTP_PROXY']

if 'https_proxy' in os.environ:
    del os.environ['https_proxy']

if 'HTTPS_PROXY' in os.environ:
    del os.environ['HTTPS_PROXY']

if 'no_proxy' in os.environ:
    del os.environ['no_proxy']
