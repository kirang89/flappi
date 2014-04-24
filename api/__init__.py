from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
db = SQLAlchemy(app)

from api import views