from ..forms import BaseForm
from wtforms import StringField,IntegerField
from wtforms.validators import Regexp,EqualTo,ValidationError,InputRequired
from utils import zlcache

class SignupForm(BaseForm):
    telephone=StringField(validators=[Regexp(r"1[345789]\d{9}",message="请输入正确格式的手机号码")]);
    sms_captcha=StringField(validators=[Regexp(r"\w{4}",message="请输入正确格式的验证码")]) #\w 包括数字和字母
    username=StringField(validators=[Regexp(r".{2,20}",message="请输入正确格式的用户名")])
    password1=StringField(validators=[Regexp(r"[0-9a-zA-Z_\.]{6,20}",message="请输入正确格式的密码")])
    password2=StringField(validators=[EqualTo("password1",message="两次输入的密码不一致")])
    graph_captcha=StringField(validators=[Regexp(r"\w{4}",message="请输入正确格式的图形验证码")])

    #validate+sms_captcha 用来验证 sms_captcha字段
    def validate_sms_captcha(self,field):
        sms_captcha=field.data
        # print("sms_captcha是",sms_captcha)
        telephone=self.telephone.data
        if sms_captcha!="1111": #测试用
            sms_captcha_mem=zlcache.get(telephone)
            # print("sms_mem是",sms_captcha_mem)
            if not sms_captcha_mem or sms_captcha_mem.lower()!=sms_captcha.lower():
                raise ValidationError(message="短信验证码验证错误")

    def validate_graph_captcha(self,field):
        graph_captcha=field.data
        # print("图形验证码是：",graph_captcha)
        if graph_captcha!="1111":
            graph_captcha_mem=zlcache.get(graph_captcha)
            # print("缓存里的图形验证码是",graph_captcha_mem)
            if not graph_captcha_mem:
                raise ValidationError(message="图形验证码错误")

class SigninForm(BaseForm):
    telephone=StringField(validators=[Regexp(r"1[345789]\d{9}",message="请输入正确格式的手机号码")])
    password=StringField(validators=[Regexp(r".{2,20}",message="请输入正确格式的密码")])
    remember=StringField()

class AddPostForm(BaseForm):
    title=StringField(validators=[InputRequired(message="请输入标题！")])
    content=StringField(validators=[InputRequired(message="请输入内容！")])
    board_id=IntegerField(validators=[InputRequired(message="请输入板块id！")])

class AddCommentForm(BaseForm):
    content=StringField(validators=[InputRequired(message="请输入评论内容")])
    post_id=IntegerField(validators=[InputRequired(message="请输入帖子id")])