from flask import Flask, request
from flask_restful import Resource, Api
from flask_restful import reqparse
import json

app = Flask(__name__)
api = Api(app)

@app.route('/')
def hello():
    return 'hello'

COMMAND_LISTS = ['list', 'show', 'add', 'delete']

class Listener(Resource):
    #To do : Try and exception, clear infinite loop

    def post(self):
        
        text = request.form.get('text')
        try:
            indicator, param = text.split(None, 1)
        else:
            indicator = text

        if(indicator == 'list'):
            api_call = Tasks()
            return api_call.get()

        else:
        	return {"text": "Sorry dude"}

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


class Tasks(Resource):
    #To do : Try and exception
    def post(self):

        return {"text": "hello universe"}

    def get(self):
    	return {"text": "Hello Universe"}

api.add_resource(Tasks, '/tasks')

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8100, debug=True)
    app.run()