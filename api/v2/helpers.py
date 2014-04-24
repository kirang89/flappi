#
# A library for helper functions
#
import hmac
from hashlib import sha1
import decimal


class Serializer(object):
    """SQLAlchemy Model JSON Serializer

    A class to help serialize sqlalchemy models
    in JSON format
    """
    __public__ = None

    def to_serializable_dict(self):
        data = {}
        for key in self.__table__.columns.keys():
            value = getattr(self, key)
            if type(value) is decimal.Decimal:
                data[key] = "%.2f" % round(float(value), 2)
            else:
                data[key] = value

        for key in self.__mapper__.relationships.keys():
            if key in self.__public__:
                if self.__mapper__.relationships[key].uselist:
                    data[key] = []
                    for item in getattr(self, key):
                        data[key].append(item.to_serializable_dict())
                else:
                    data[key] = getattr(self, key)

        return data


def get_signature(secret_key, request=None, message=None):
    """Generate signature

    Method to sign a http request using HMAC
    """
    if request:
        message = request.path + request.method + request.headers['Content-Type']

    print "THE MESSAGE: ", message
    print secret_key
    signature = hmac.new(secret_key, message, sha1)
    return signature.hexdigest()
