from flask import Flask
from flask_sqlalchemy import SQLAlchemy

## this init file means that the app folder is a module

## parameter __name__ is usually the name of the module you are in.
## in this case, app
app = Flask(__name__)
app.config.from_object('config')

from app import views
