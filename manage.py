from flask import current_app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import db, create_app

# 创建app，并传入配置模式：development/production
app = create_app("development")

manager = Manager(app)  # Flask-script
Migrate(app, db)  # 数据库迁移
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():
    current_app.logger.debug("debug")
    current_app.logger.error("error")
    return "hello"


if __name__ == '__main__':
    # app.run()
    manager.run()
