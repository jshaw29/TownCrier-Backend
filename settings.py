from os.path import join, dirname
from dotenv import load_dotenv
import os
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
DATABASE_URL = os.environ.get("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS =  os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
SECRET_DELETE_KEY = os.environ.get("SECRET_DELETE_KEY")