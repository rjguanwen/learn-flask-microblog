from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
# 从config加载配置
app.config.from_object('config')
db = SQLAlchemy(app)

# 创建
lm = LoginManager()
# 初始化
lm.init_app(app)
lm.login_view = 'login'

from app import views, models
