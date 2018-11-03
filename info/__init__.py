import logging
from logging.handlers import RotatingFileHandler

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
    setup_log(config_name)  # 配置项目日志
    app = Flask(__name__)

    app.config.from_object(config[config_name])  # 配置，是config.py文件中的字典config
    db.init_app(app)  # 配置数据库
    global redis_store
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_PORT, port=config[config_name].REDIS_PORT)  # 配置redis
    CSRFProtect(app)  # 开启csrf保护
    Session(app)  # 设置session保存位置

    return app


def setup_log(config_name):
    """配置日志"""

    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式、日志等级、输入日志信息的文件名、行数、日志信息
    formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
