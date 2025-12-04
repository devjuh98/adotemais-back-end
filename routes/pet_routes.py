from flask import Blueprint, request, jsonify
from controllers.pet_controller import create_pet, list_pets, list_user_pets

pet_bp = Blueprint('pet_bp', __name__)

@pet_bp.route('/pets', methods=['POST'])
def route_create_pet():
    return create_pet(request)

@pet_bp.route('/pets', methods=['GET'])
def route_list_pets():
    return list_pets()

@pet_bp.route('/users/<user_id>/pets', methods=['GET'])
def route_list_user_pets(user_id):
    return list_user_pets(user_id)