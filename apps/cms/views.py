import random
import string

from flask import (
    Blueprint,
    views,
    render_template,
    request, session,
    redirect,
    url_for,
    g,
    jsonify

)
from .forms import (
    LoginForm,
    ResetpwdForm,
    ResetemailForm,
    AddBannerForm,
    UpdateBannerForm,
    AddBoardForm,
    UpdateBoardForm
)

from .models import CMSUser, CMSPermission
from ..models import  BannerModel,BoardModel,PostModel,HighLightPostModel
from .decorators import login_required, permission_required
import config
from exts import db,mail
from utils import restful,zlcache
from flask_mail import Message
from tasks import send_mail


bp=Blueprint("cms",__name__,url_prefix="/cms")

@bp.route('/')
@login_required
def index():
    return render_template('cms/cms_index.html')


@bp.route('/logout/')
@login_required
def logout():
    #session.clear()
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template("cms/cms_profile.html")


@bp.route('/email_captcha/')
@login_required
def email_captcha():
    email=request.args.get('email')
    if not email:
        return restful.params_error('没有邮箱，请传递邮箱参数！')
    source=list(string.ascii_letters)
    # source.extend(["0","1",'2','3','4','5','6','7','8','9'])
    source.extend(map(lambda x:str(x),range(0,10)))
    # 随机采样,返回列表,并将列表转换成字符串
    captcha="".join(random.sample(source,6))
    #给这个邮箱发送邮件
    # message=Message("python论坛邮箱验证码",recipients=[email],body="您的验证码是：%s"%captcha)
    # try:
    #     mail.send(message)
    # except:
    #     return restful.server_error()
    send_mail.delay("python论坛邮箱验证码", [email], body="您的验证码是：%s" % captcha)
    zlcache.set(email,captcha)
    return restful.success()


@bp.route('/email/')
def send_email():
    message=Message("邮件发送",recipients=['294714025@qq.com'],body="测试")
    mail.send(message)
    return "success"


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    post_list=PostModel.query.all()
    return  render_template('cms/cms_posts.html',posts=post_list)

@bp.route('/hpost/',methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def hpost():
    post_id=request.form.get('post_id')
    if not post_id:
        return restful.params_error("请输入帖子id")
    post=PostModel.query.get(post_id)
    if not post:
        return restful.params_error("没有这篇帖子")
    highlight=HighLightPostModel()
    highlight.post=post
    db.session.add(highlight)
    db.session.commit()
    return restful.success()

@bp.route('/uhpost/',methods=['POST'])
@login_required
@permission_required(CMSPermission.POSTER)
def uhpost():
    post_id=request.form.get('post_id')
    if not post_id:
        return restful.params_error("请输入帖子id")
    post=PostModel.query.get(post_id)
    if not post:
        return restful.params_error("没有这篇帖子")
    highlight=HighLightPostModel.query.filter_by(post_id=post_id).first()
    db.session.delete(highlight)
    db.session.commit()
    return restful.success()


@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return  render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    board_models=BoardModel.query.all()
    context={
        "boards":board_models
    }
    return  render_template('cms/cms_boards.html',**context)


@bp.route('/aboard/',methods=["POST"])
@login_required
@permission_required(CMSPermission.BOARDER)
def aboard():
    form=AddBoardForm(request.form)
    if form.validate():
        name=form.name.data
        board=BoardModel(name=name)
        db.session.add(board)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())

@bp.route('/uboard/',methods=["POST"])
@login_required
@permission_required(CMSPermission.BOARDER)
def uboard():
    # print(request.form.board_id.data)
    form=UpdateBoardForm(request.form)
    if form.validate():
        board_id=form.board_id.data
        name=form.name.data
        board=BoardModel.query.get(board_id)
        if board:
            board.name=name
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message="没有这个板块!")
    else:
        return restful.params_error(message=form.get_error())
@bp.route('/dboard/',methods=['POST'])
@login_required
@permission_required(CMSPermission.BOARDER)
def dboard():
    board_id=request.form.get('board_id')
    if not board_id:
        return restful.params_error(message="请传入板块id!")
    board=BoardModel.query.get(board_id)
    if not board:
        return restful.params_error(message="这个板块不存在")
    db.session.delete(board)
    db.session.commit()
    return restful.success()


@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTUSER)
def fusers():
    return  render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return  render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def croles():
    return  render_template('cms/cms_croles.html')


@bp.route('/banners/')
@login_required
def banners():
    banners=BannerModel.query.all()
    return render_template("cms/cms_banners.html",banners=banners)


@bp.route("/abanner/",methods=['POST'])
@login_required
def abanner():
    form=AddBannerForm(request.form)
    if form.validate():
        name=form.name.data
        image_url=form.image_url.data
        link_url=form.link_url.data
        priority=form.priority.data
        banners=BannerModel(name=name,image_url=image_url,link_url=link_url,priority=priority)
        db.session.add(banners)
        db.session.commit()
        return restful.success()
    else:
        return restful.params_error(message=form.get_error())


@bp.route("/ubanner/",methods=['POST'])
@login_required
def ubanner():
    form=UpdateBannerForm(request.form)
    if form.validate():
        banner_id=form.banner_id.data
        name=form.name.data
        image_url=form.image_url.data
        link_url=form.link_url.data
        priority=form.priority.data
        banner=BannerModel.query.get(banner_id)
        if banner:
            banner.name=name
            banner.image_url=image_url
            banner.link_url=link_url
            banner.priority=priority
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message="没有这个轮播图！")
    else:
        return restful.params_error(message=form.get_error())


@bp.route("/dbanner/",methods=['POST'])
@login_required
def dbanner():
    banner_id=request.form.get("banner_id")
    if not banner_id:
        return  restful.params_error(message="请传入轮播图id!")
    banner=BannerModel.query.get(banner_id)
    if not banner:
        return restful.params_error(message="没有这个轮播图！")
    db.session.delete(banner)
    db.session.commit()
    return restful.success()



class ResetPwdView(views.MethodView):
    decorators=[login_required]
    def get(self):
        return render_template('cms/cms_resetpwd.html')
    def post(self):
        form=ResetpwdForm(request.form)
        if form.validate():
            oldpwd=form.oldpwd.data
            newpwd=form.newpwd.data
            user=g.cms_user
            if user.check_password(oldpwd):
                user.password=newpwd
                db.session.commit()
                #返回前端的数据格式 {"code":**,""message":"",}
                return restful.success()
            else:
                return restful.params_error("旧密码错误")
        else:
            message=form.get_error()
            return restful.params_error(form.get_error())




class LoginView(views.MethodView):
    def get(self,message=None):
        return  render_template('cms/cms_login.html',message=message)

    def post(self):
        form=LoginForm(request.form)
        if form.validate():
            email=form.email.data
            password=form.password.data
            remember=form.remember.data
            user=CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID]=user.id
                if remember:
                    #如果设置session.perma1nent=True，那么过期时间是31天
                    session.permanent=True
                return redirect(url_for('cms.index'))
            else:
                return self.get(message="邮箱或者验证码错误")
        else:
            # print(form.errors) form.errors 为字典 {'password': ['请输入正确格式的密码'],"email":"**@qq.com"}
            #字典中的第二个元素为列表，然后取列表中的第一个值 popitem可以返回字典中的任意一项
            # message=form.errors.popitem()[1][0]
            message=form.get_error()
            return self.get(message=message)

class ResetEmailView(views.MethodView):
    decorators=[login_required]
    def get(self):
        return render_template('cms/cms_resetemail.html')
    def post(self):
        form=ResetemailForm(request.form)
        if form.validate():
            email=form.email.data
            g.cms_user.email=email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())
        # email=
        # captcha=
bp.add_url_rule('/login/',view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/',view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/',view_func=ResetEmailView.as_view('resetemail'))