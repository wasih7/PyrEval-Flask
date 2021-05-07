from flask import Flask
from flask import request
# Wasih 05-07-21: Don't know why PyrEval appears as Pyreval sometimes
from Pyreval.pyreval_flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getIndividualScore', methods=['POST', 'GET'])
def test():
    error = None
    config_path = '/home/wasih7/pyreval-flask-main/PyrEval/parameters.ini'
    if request.method == 'POST':
        try:
            rf = dict(request.form)
            print(getIndividualScoreFunc(rf["answer"]))
            return "post return"
        except:
            return "failed post return"
    else:
        return "other queries return"

