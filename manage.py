from flask.ext.script import Manager

from api import app, db

manager = Manager(app)


@manager.command
def run_dev_server():
    """Run application in development mode"""
    app.run(host='127.0.0.1', port=5000, debug=True)


@manager.command
def run_prod_server():
    """Run application in production mode"""
    app.run(host='0.0.0.0', port=8080)


@manager.command
def create_db():
    """Creates database and necessary tables"""
    db.create_all()


if __name__ == '__main__':
    manager.run()
