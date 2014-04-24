from flask.ext.testing import TestCase
from api import db
from api.models import User
from api.helpers import get_signature
from flask import Flask

BASE_URL = "http://127.0.0.1:5000"


class MyTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        return app

    def setUp(self):
        db.create_all()
        self.user = User(email="k@gmail.com", password="1234")
        self.user.api_key = '9dff2e6aeb1c4ec7b5e2d6d65fd569ef'
        self.user.secret_access_key = '2f4c80fd51ea488e8c6cfcacbc073696'
        db.session.add(self.user)
        db.session.commit()

    def get_headers(self, api_key, sak, msg):
        return {
            'Content-Type': 'application/json',
            'Authorization': "%s:%s" % (api_key, get_signature(sak, message=msg))
        }

    def test_basic(self):
        assert 1 + 1 == 2

    #
    # Add tests here
    #

    def tearDown(self):
        db.session.remove()
        db.drop_all()
