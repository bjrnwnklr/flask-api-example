from flask import Flask
from config import Config
from flask_restful import Resource, Api
from flaskapi.api import HelloWorld

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

api.add_resource(HelloWorld, '/')

# do any additional configuration stuff, instantiation (e.g. of DBs, encryption, API objects) here
# and import them in the respective modules.

# this has to be at the bottom to avoid circular references
# from flaskapi import routes

