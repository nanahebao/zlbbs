from apps.forms import BaseForm
from wtforms import StringField
from wtforms.validators import regexp,InputRequired
import hashlib

class SMSCaptchaForm(BaseForm):
    salt='dfurtn5hdsesjc*&^nd'
    telephone=StringField(validators=[regexp(r'1[3578]\d{9}')])
    timestamp=StringField(validators=[regexp(r'\d{13}')])
    sign=StringField(validators=[InputRequired()])

    def validate(self):
        result=super(SMSCaptchaForm, self).validate()
        if not result:
            return False
        telephone=self.telephone.data
        timestamp=self.timestamp.data
        sign=self.sign.data

        sign2=hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest() #hexdigest把二进制转换成字符串
        # print("客户端提交的签名：",sign)
        # print("服务器设生成的签名:",sign2)
        if sign==sign2:
            return True
        else:
            return False

# from apps.forms import BaseForm
# from wtforms import StringField
# from wtforms.validators import regexp,InputRequired
# import hashlib
#
# class SMSCaptchaForm(BaseForm):
#     salt='jiejigheie98378od`#$'
#     telephone=StringField(validators=[regexp(r'1[34579]\d{9}')])
#     timestamp=StringField(validators=[regexp(r'\d{13}')])
#     sign=StringField(validators=[InputRequired()])
#
#     def validate(self):
#         result=super(SMSCaptchaForm,self).validate()
#         if not  result:
#             return False
#         telephone=self.telephone.data
#         timestamp=self.timestamp.data
#         sign=self.sign.data
#         #md5必须要传一个bytes类型的字符串进去
#         sign2=hashlib.md5((timestamp+telephone+self.salt).encode('utf-8')).hexdigest()
#         if sign==sign2:
#             return True
#         else:
#             return False

