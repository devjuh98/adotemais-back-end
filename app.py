from flask import Flask
from flask_cors import CORS
from routes.pet_routes import pet_bp
from routes.user_routes import user_bp   

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_bp)
app.register_blueprint(user_bp)

@app.route('/')
def home():
    return "Servidor Flask rodando com MongoDB local!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)