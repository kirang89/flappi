#
# ERROR HANDLERS
#

import json
from flask import jsonify, Response
from api import app


@app.errorhandler(404)
def not_found(error=None, url=''):
    message = {
        'status': 404,
        'message': 'Not Found: ' + url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

app.error_handler_spec[None][404] = not_found


@app.errorhandler(500)
def internal_error(e=None):
    return Response(json.dumps({"error": "Something went wrong"}),
                    status=500,
                    mimetype='application/json')


@app.errorhandler(401)
def not_authorized(error=None, url=''):
    message = {
        'status': 401,
        'message': 'Unauthorized Request',
        'url': url
    }
    return Response(json.dumps(message),
                    status=401,
                    mimetype='application/json')


@app.errorhandler(405)
def method_unexpected(error=None, url=''):
    message = {
        'status': 405,
        'message': 'Request method not expected',
        'url': url
    }
    return Response(json.dumps(message),
                    status=405,
                    mimetype='application/json')


@app.errorhandler(400)
def bad_request(error=None, url=''):
    text = 'A required query parameter was not specified for this request.'
    if error:
        text = error
    message = {
        'status': 400,
        'message': text,
        'url': url
    }
    return Response(json.dumps(message),
                    status=400,
                    mimetype='application/json')
