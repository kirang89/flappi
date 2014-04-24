import json
from flask import Response
from v1.views import api_v1
from v2.views import api_v2
from api import app, db
from api.errors import *


app.register_blueprint(api_v1, url_prefix='/v1')
app.register_blueprint(api_v2, url_prefix='/v2')


@app.route('/', methods=['GET'])
def index():
    data = {
        "message": "Welcome to my API :)"
    }
    return Response(json.dumps(data),
                    200,
                    mimetype='application/json')
