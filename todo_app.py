from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
import json

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return 'hello'

class Listener(Resource):
    #To do : Try and exception
    def post(self):
        
        indicator = request.form.get('text')
        if(indicator == 'list'):
            api_call = Listener2()
            return api_call.post()

        #return {"text": json.dumps(request.form)}
"""
request.form has follwing dictionary

{"token": "51Ep36kP6jZ0owNweBV7EfZ2", "team_id": "T0T9YUDFA", 
"team_domain": "gcm-infra", "service_id": "473395518851", 
"channel_id": "CDWNAEGSC", "channel_name": "bot-test", 
"timestamp": "1541589611.006100", "user_id": "UDT51DG3V", 
"user_name": "daul.chung", "text": "list", "trigger_word": "list"}
"""

api.add_resource(Listener, '/listener')


class Listener2(Resource):
    #To do : Try and exception
    def post(self):

        return {"text": "hello universe"}

api.add_resource(Listener2, '/listener2')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8100, debug=True)
    app.run()