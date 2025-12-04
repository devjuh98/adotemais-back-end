from flask import request, jsonify
from pymongo import MongoClient
from utils.auth import hash_password, check_password, generate_token
import uuid

client = MongoClient('mongodb://localhost:27017/AdoteMais')
db = client['AdoteMais']
users_collection = db['users']

def register_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    name = data.get('name')
    biography = data.get('biography') 

    if users_collection.find_one({'email': email}):
        return jsonify({'error': 'Email já cadastrado'}), 400

    hashed_pw = hash_password(password)
    new_user = {
        'id': str(uuid.uuid4()),
        'name': name,
        'email': email,
        'password': hashed_pw,
        'biography': biography 
    }
    users_collection.insert_one(new_user)
    return jsonify({'message': 'Usuário cadastrado com sucesso'}), 201

def login_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = users_collection.find_one({'email': email})
    if not user or not check_password(password, user['password']):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    token = generate_token(user['id'])
    return jsonify({
        'token': token,
        'user_id': user['id'],
        'name': user['name'],
        'biography': user.get('biography') 
    }), 200