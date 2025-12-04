from flask import request, jsonify
from pymongo import MongoClient
from datetime import datetime
import uuid

client = MongoClient('mongodb://localhost:27017/AdoteMais')
db = client['AdoteMais']
pets_collection = db['pets']

def create_pet(req):
    data = req.get_json() or {}

    # lista de campos obrigatórios
    required_fields = ['name', 'specie', 'breed', 'age', 'description', 'image', 'userId']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"Campo obrigatório '{field}' não informado"}), 400

    new_pet = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'specie': data['specie'],
        'breed': data['breed'],
        'age': data['age'],
        'description': data['description'],
        'image': data['image'],
        'owner': data['userId'],  # consistência: "owner" = usuário dono do pet
        'created_at': datetime.utcnow()
    }

    pets_collection.insert_one(new_pet)
    new_pet['_id'] = None  # remove o campo interno do Mongo
    return jsonify(new_pet), 201

def list_pets():
    # ordena por data de criação (mais recentes primeiro)
    pets = list(pets_collection.find({}, {'_id': 0}).sort('created_at', -1))
    return jsonify(pets)

def list_user_pets(user_id):
    # ordena também os pets do usuário
    pets = list(pets_collection.find({'owner': user_id}, {'_id': 0}).sort('created_at', -1))
    return jsonify(pets)