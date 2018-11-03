from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/flask04_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
app.config.from_object(Config)
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "hello"


if __name__ == '__main__':
    app.run()
