import redis
from flask import Flask
from flask.ext.wtf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)  # 配置
db = SQLAlchemy(app)  # 配置数据库
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)  # 配置redis
CSRFProtect(app)  # 开启csrf保护
Session(app)  # 设置session保存位置
