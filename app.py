from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # permite que o React acesse a API Flask

# banco de dados em memória (lista de pets)
pets = []

# rota para criar uma publicação de pet para adoção
@app.route('/pets', methods=['POST'])
def create_pet():
    data = request.get_json()
    new_pet = {
        'id': len(pets) + 1,
        'name': data.get('name'),
        'specie': data.get('specie'),
        'breed': data.get('breed'),
        'age': data.get('age'),
        'description': data.get('description'),
        'image': data.get('image')
    }
    pets.append(new_pet)
    return jsonify(new_pet), 201

@app.route('/pets', methods=['GET'])
def list_pets():
    return jsonify(pets)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)