import requests
def send(mobile,captcha):
    url="http://v.juhe.cn/sms/send"
    params={
        "mobile":mobile,
        "tpl_id":"121674",
        "tpl_value":"#code#"+captcha,
        "key":"jiheihgeihge29385",
    }

    response=requests.get(url,params=params)
    result=response.json()
    if result['error_code']==0:
        return True
    else:
        return False