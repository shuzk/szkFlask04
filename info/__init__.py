import redis
from flask import Flask
from flask.ext.wtf import CSRFProtect
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# from config import Config
from config import config

# app = Flask(__name__)
#
# app.config.from_object(Config)  # 配置
# db = SQLAlchemy(app)  # 配置数据库
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)  # 配置redis
# CSRFProtect(app)  # 开启csrf保护
# Session(app)  # 设置session保存位置

# 数据库
db = SQLAlchemy()
redis_store = None


def create_app(config_name):
    """通过传入不同的配置名字，初始化其对应配置的应用实例"""
    app = Flask(__name__)

    app.config.from_object(config[config_name])  # 配置，是config.py文件中的字典config
    db.init_app(app)  # 配置数据库
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_PORT, port=config[config_name].REDIS_PORT)  # 配置redis
    CSRFProtect(app)  # 开启csrf保护
    Session(app)  # 设置session保存位置

    return app
