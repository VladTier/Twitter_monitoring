from flask_migrate import MigrateCommand
from flask_script import Manager
from app.app import create_app
from app.views import login_manager

app = create_app()

login_manager.init_app(app)

manager = Manager(app)

manager.add_command('db', MigrateCommand)


import app.views

if __name__ == "__main__":
    manager.run()
