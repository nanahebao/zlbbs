# common/views.py
from io import BytesIO

__author__ = 'derek'

from flask import Blueprint, request, make_response
from exts import alidayu
from utils import restful, zlcache
from utils.captcha import Captcha
from .forms import SMSCaptchaForm
from tasks import send_sms_captcha

bp = Blueprint("common",__name__,url_prefix='/c')

@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
#     telephone+timestamp+salt
    form=SMSCaptchaForm(request.form)
    if form.validate():
        telephone=form.telephone.data
        captcha=Captcha.gene_text(numbers=4).replace(" ","")
        print("发送的验证码是：",captcha)
        send_sms_captcha(telephone,captcha)
        # if alidayu.send_sms(telephone,code=captcha):
        #     #手机号码作为key，验证码作为value存到memcache中
        #     zlcache.set(telephone,captcha)
        #     return restful.success()
        # else:
        #      # return restful.paramas_error(message='参数错误')
        #      #开发中，失败的时候也写入进memcache
        #     zlcache.set(telephone,captcha)
        #     return restful.success()
    else:
        return restful.params_error(message='参数错误')

@bp.route('/captcha/')
def graph_captcha():
    #获取验证码
    text,image=Captcha.gene_graph_captcha()
    zlcache.set(text.replace(" ","").lower(),text.replace(" ","").lower()) #text.replece(" ","")去掉空格
    #ByteIo：字节流 （必须用二进制流的形式才能在网络上传输） 保存在内存中
    out=BytesIO()
    image.save(out,'png') #保存的格式是png
    out.seek(0) #把文件流的指针放到最开始的位置
    resp=make_response(out.read()) #创建response对象
    resp.content_type='image/png'#response的数据类型
    return resp