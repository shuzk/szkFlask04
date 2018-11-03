import redis
from config import Config
from flask import Flask
from flask_session import Session
from flask.ext.wtf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
CSRFProtect(app)
Session(app)
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "hello"


if __name__ == '__main__':
    # app.run()
    manager.run()