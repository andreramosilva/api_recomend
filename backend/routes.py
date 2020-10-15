
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


        # if  not data:
        #     abort(404)

        # if not request.get_json():
        #     abort(400)
        # data = request.get_json(force=True)

        # if not data.get(data['nome']):
        #     abort(400)
        # if not validate_email(data['amigo']):
        #     abort(400)

        result = storage.populate(data['nome'],data['amigo'])
        return jsonify(result,201)
       
        #return jsonify(BOOK_REQUESTS[_id]), 200



# @REQUEST_API.route('/request', methods=['GET'])
# def get_records():
#     """Return all book requests
#     @return: 200: an array of all known BOOK_REQUESTS as a \
#     flask/response object with application/json mimetype.
#     """
#     return x(BOOK_REQUESTS)


# @REQUEST_API.route('/request/<string:_id>', methods=['GET'])
# def get_record_by_id(_id):
#     """Get book request details by it's id
#     @param _id: the id
#     @return: 200: a BOOK_REQUESTS as a flask/response object \
#     with application/json mimetype.
#     @raise 404: if book request not found
#     """
#     if _id not in BOOK_REQUESTS:
#         abort(404)
#     return jsonify(BOOK_REQUESTS[_id])


# @REQUEST_API.route('/request', methods=['POST'])
# def create_record():
#     """Create a book request record
#     @param email: post : the requesters email address
#     @param title: post : the title of the book requested
#     @return: 201: a new_uuid as a flask/response object \
#     with application/json mimetype.
#     @raise 400: misunderstood request
#     """
#     if not request.get_json():
#         abort(400)
#     data = request.get_json(force=True)

#     if not data.get('email'):
#         abort(400)
#     if not validate_email(data['email']):
#         abort(400)
#     if not data.get('title'):
#         abort(400)

#     new_uuid = str(uuid.uuid4())
#     book_request = {
#         'title': data['title'],
#         'email': data['email'],
#         'timestamp': datetime.now().timestamp()
#     }
#     BOOK_REQUESTS[new_uuid] = book_request
#     # HTTP 201 Created
#     return jsonify({"id": new_uuid}), 201


# @REQUEST_API.route('/request/<string:_id>', methods=['PUT'])
# def edit_record(_id):
#     """Edit a book request record
#     @param email: post : the requesters email address
#     @param title: post : the title of the book requested
#     @return: 200: a booke_request as a flask/response object \
#     with application/json mimetype.
#     @raise 400: misunderstood request
#     """
#     if _id not in BOOK_REQUESTS:
#         abort(404)

#     if not request.get_json():
#         abort(400)
#     data = request.get_json(force=True)

#     if not data.get('email'):
#         abort(400)
#     if not validate_email(data['email']):
#         abort(400)
#     if not data.get('title'):
#         abort(400)

#     book_request = {
#         'title': data['title'],
#         'email': data['email'],
#         'timestamp': datetime.now().timestamp()
#     }

#     BOOK_REQUESTS[_id] = book_request
#     return jsonify(BOOK_REQUESTS[_id]), 200


