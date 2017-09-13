from flask import Flask
from flask_restful import Resource, Api
from controller.helloworld import HelloWorld as HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
