from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
import towncrier.routes.post_route
import towncrier.models.post_db