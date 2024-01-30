import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load .env file
dotenv_path = join(dirname(__file__), 'vars.env')
load_dotenv(dotenv_path)

# ENVEIRONMENT VARIABLES
PROJECT_ID = os.environ.get('PROJECT_ID')
BUCKET_NAME = os.environ.get('BUCKET_NAME')
SECRET_KEY = os.environ.get('SECRET_KEY')