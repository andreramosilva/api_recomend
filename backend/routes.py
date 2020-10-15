
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from Storage import * 

# from validate_email import validate_email
REQUEST_API = Blueprint('request_api', __name__)
storage = Storage()

def get_blueprint():
    """Return the blueprint for the main REQUEST_API module"""
    return REQUEST_API


#rotas aqui : 
@REQUEST_API.route("/show_all_users",methods=['GET'])
def show_all_users():
        result = storage.show_all_users()
        return jsonify(result,200)
        

@REQUEST_API.route("/show_friends",methods=['GET'])
def show_friends():
        data = request.get_json()
        result = storage.show_all_friends(data['nome'])
        return jsonify(result,200)
        


@REQUEST_API.route("/show_friend_recomendation",methods=['GET'])
def show_friend_recomendation():
        
        data = request.get_json()
        result = storage.show_recomendation(data['nome'])
        return jsonify(result,200)

@REQUEST_API.route("/register_new_user/",methods=['POST'])
def register_new_user():
        data = request.get_json()


        result = storage.populate(data['nome'],data['amigo'])
        return jsonify(result,201)
       
 