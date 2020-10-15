
import os
import requests
from flask import Flask, request, jsonify, json ,render_template ,make_response
from Storage import Storage 
from flask_swagger_ui import get_swaggerui_blueprint
import argparse
from flask_cors import CORS
from routes import *
#from Storage import * 


APP = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Python Flask REST API"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

# storage = Storage()

# print(storage.show_all_friends("ana"))


APP.register_blueprint(get_blueprint())


@APP.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@APP.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@APP.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@APP.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        APP.run(host='0.0.0.0', port=PORT, debug=False)





# # app.register_blueprint(request_api.get_blueprint())

# # @app.route("/swagger/api")
# # def swagger_api():    
# #     with open("public/swagger.yaml", "r") as f:
# #         content = f.read()
# #     return "<pre>"+content+"</pre>"

# # @app.route("/explorer")
# # def explorer():
# #     return render_template('swagger-ui/index.html')

# if __name__ == '__main__':
#     app.run(debug=True, use_reloader=True)



