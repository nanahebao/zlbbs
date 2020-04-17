import os

SECRET_KEY=os.urandom(24)
SECRET_KEY="diehgiehgeigeg"

DEBUG=True

# HOSTNAME="172.27.0.78"
HOSTNAME="172.27.0.108"
PORT="6033"
DATABASE="zlbbs"
USERNAME="root"
PASSWORD="123456"

#PERMERNENT_SESSION_LIFETIME

DB_URI="mysql+pymysql://{username}:{password}@{hostname}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD,
        hostname=HOSTNAME,port=PORT,db=DATABASE)

SQLALCHEMY_DATABASE_URI=DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS=False

CMS_USER_ID='IJIIGHIEHGIHGIEH'
FRONT_USER_ID="jihehegihegeghei"

#邮件配置
#发送者邮箱的服务器地址
MAIL_SERVER ='smtp.qq.com'
# MAIL_PORT='587'
MAIL_PORT='465'
# MAIL_USE_TLS =True
MAIL_USE_SSL=True
# MAIL_DEBUG = default app.debug
MAIL_USERNAME = "294714025@qq.com"
MAIL_PASSWORD = "bekoqmhcuhuccbcj"
MAIL_DEFAULT_SENDER = "294714025@qq.com"


ALIDAYU_APP_KEY = '23709557'
ALIDAYU_APP_SECRET = 'd9eiehigehg97hdeg'
ALIDAYU_SIGN_NAME = '仙剑论坛网站'
ALIDAYU_TEMPLATE_CODE = 'SMS_136xxx947'

#UEditor的相关配置
import os

import os

# 这是讲文件上传到本地服务器的images下
# config所在的路径os.path.dirname(__file__)
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


# # 这是配置的上传到七牛的, 你配置了这个那么文件就会直接上传到七牛
# UEDITOR_UPLOAD_TO_QINIU = True
# # AccessKey
# UEDITOR_QINIU_ACCESS_KEY = "*****************************************"
# # SecretKey
# UEDITOR_QINIU_SECRET_KEY = "*****************************************"
# # 上传的空间名称
# UEDITOR_QINIU_BUCKET_NAME = "********"
# # 域名 七牛的域名  也可以用七牛给的测试域名
# UEDITOR_QINIU_DOMAIN = "http://***************/"

#flask-paginate的相关配置
PER_PAGE=10
#celery相关的配置
CELERY_RESULT_BACKEND="redis://:123456@127.0.0.1:6379/0"
CELERY_BROKER_URL="redis://:123456@127.0.0.1:6379/0"