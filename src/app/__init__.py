from flask import Flask
from flask_jwt_extended import JWTManager
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

from app import routes