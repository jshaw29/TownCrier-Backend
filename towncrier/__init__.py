from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
import towncrier.routes.post_route
import towncrier.models.post_db