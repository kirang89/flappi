import json
import uuid
from api import db


class User(db.Model):
    __tablename__ = 'users'

    # Fields that appear in serialized model
    __public__ = ['id', 'api_key', 'email', 'password',
                  'type', 'phone_number', 'customers', 'products']

    # Fields that cannot be updated
    __no_overwrite__ = ['id', 'secret_access_key', 'products']

    id = db.Column(db.String(32), primary_key=True, default=str.encode(uuid.uuid4().hex, 'utf8'))
    email = db.Column(db.String(100))
    password = db.Column(db.String(20))
    api_key = db.Column(db.String(32), default=uuid.uuid4().hex)
    secret_access_key = db.Column(db.String(32), default=uuid.uuid4().hex)

    # Function to update columns
    def update(self, **kwargs):
        columns = self.__table__.columns.keys()
        for key, value in kwargs.items():
            if key in columns and (key not in self.__no_overwrite__):
                setattr(self, key, value)

    def to_json(self):
        return json.dumps(self.to_serializable_dict())
