from flask import Flask
from apps.cms import bp as cms_bp
from apps.common import bp as common_bp
from apps.front import bp as front_bp
from apps.ueditor import bp as editor_bp
import config
from exts import db,mail,alidayu
from flask_wtf import CSRFProtect
# from utils.captcha import Captcha
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(cms_bp)
    app.register_blueprint(common_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(editor_bp)
    db.init_app(app)
    mail.init_app(app)
    alidayu.init_app(app)
    CSRFProtect(app)
    return app


#1，配置文件conf.py 、exts.py 、 modles.py、manage.py
#前台，后台，公共的
#在主app中不写任何视图，都分布在cms。common。front中

# Captcha.gene_graph_captcha()

if __name__ == '__main__':
    app=create_app()
    app.run()
