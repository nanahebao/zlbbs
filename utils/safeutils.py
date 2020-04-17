from urllib.parse import urlparse,urljoin
from flask import  request,url_for
def is_safe_url(target):
    ref_url=urlparse(request.host_url) #urlparse可以将url分成域名部分。。
    test_url=urlparse(urljoin(request.host_url,target))
    return test_url.scheme in ("http","https") and \
        ref_url.netloc==test_url.netloc #比较域名


