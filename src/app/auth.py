from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
import jwt

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'default_jwt_secret' 

jwt = JWTManager(app)

@app.route('/set-client-secret', methods=['POST'])
def set_client_secret():
    client_secret = request.json.get('client_secret', None)
    
    if client_secret:
        app.config['JWT_SECRET_KEY'] = client_secret
        return jsonify({"msg": "Client secret set successfully"}), 200
    else:
        return jsonify({"msg": "Client secret is required"}), 400

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if username == "admin" and password == "admin":
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    
    return jsonify({"msg": "Bad credentials"}), 401

def is_token_rs256(token):
    
    header = jwt.get_unverified_header(token)

    if header.get("alg") == "RS256":
        return True
    else:
        return False
    

if __name__ == '__main__':
    app.run(debug=True)
