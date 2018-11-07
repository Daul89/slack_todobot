from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return 'hello'

class Listener(Resource):
    #To do : Try and exception
    def post(self, **kwargs):
        return {"text": "yes my lord"+kwargs}

api.add_resource(Listener, '/listener')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8100, debug=True)
    app.run()