
import os
import requests
from flask import Flask, request, jsonify, json
from Storage import Storage 





app = Flask(__name__)

#rotas aqui : 
@app.route("/show_all_users",methods=['GET'])
def show_all_users():
        result = Storage.show_all_users()
        return result,200

@app.route("/show_friends/<nome>",methods=['GET'])
def show_friends(nome):
        result = Storage.show_all_friends()
        return result,200


@app.route("/show_friend_recomendation/<nome>",methods=['GET'])
def show_friend_recomendation(nome):
        result = Storage.show_recomendation()
        return result,200

@app.route("/register_new_user/",methods=['POST'])
def register_new_user(nome):
        data = request.get_json()
        result = Storage(data.nome,data.amigo)
        return data,201

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



