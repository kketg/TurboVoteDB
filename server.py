from flask import *
import requests
from database import db
import json
from userdatabase import userdb
app = Flask(__name__)

data = db()
userData = userdb()

stylesheet = open("templates/stylesheet.css").read()

@app.route('/portal')
def index():
    return render_template("template.html", css=stylesheet, header="Index", content="")

@app.route('/portal/<id>')
def getPollingPlace(id):
    return render_template("template.html", css=stylesheet, header=id, content="yeetfornow")

@app.route('/db')
def wholeboi():
    return str(data.toJSON()).replace("'","\"")
@app.route('/db/query/<id>')
def queryPollingLocation(id):
    return data.searchDb(id)
@app.route('/db/query/time/<id>')
def queryWaitTime(id):
    dic = data.searchDb(id)
    return dic["currentWaitTime"]
@app.route('/db/append/<id>/<name>', methods=['POST'])
def addToDb(id, name):
    newDict = {"id": id, "name": name}
    data.addToDb(newDict)
    return newDict
@app.route('/users')
def users():
    return str(userData.toJSON()).replace("'","\"")
@app.route('/users/register/<id>/<pw>/<maxTime>/<location>', methods=['POST'])
def register(id,pw,maxTime,location):
    thing = {"id": id, "password": pw, "maxtime": maxTime, "location": location}
    userData.addToDb(thing)
    return thing



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9090)