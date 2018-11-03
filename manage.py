from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from info import app, db

manager = Manager(app)  # Flask-script
Migrate(app, db)  # 数据库迁移
manager.add_command("db", MigrateCommand)


@app.route("/")
def index():
    return "hello"


if __name__ == '__main__':
    # app.run()
    manager.run()
