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
    return render_template("template.html", css=stylesheet, header=id, content=data.searchDb(int(id)))

@app.route('/db')
def wholeboi():
    return str(data.toJSON()).replace("'","\"")
@app.route('/db/query/<id>')
def queryPollingLocation(id):
    return str(data.searchDb(int(id))).replace("'","\"")
@app.route('/db/query/name/<id>')
def queryWaitTime(id):
    dic = data.searchDb(int(id))
    name = dic["name"]
    return str(name)
@app.route('/db/query/time/<id>')
def queryWaitTime(id):
    dic = data.searchDb(int(id))
    time = dic["currentWaitTime"]
    return str(time)
@app.route('/db/post/time/<id>/<time>', methods=['POST'])
def postCurrentTime(id,time):
    return data.changeCurrentTime(int(id),int(time))
@app.route('/db/post/new/<id>/<name>/<time>', methods=['POST'])
def addToDb(id, name, time):
    newDict = {"id": int(id), "name": name, "currentWaitTime": int(time)}
    data.addToDb(newDict)
    return newDict
@app.route('/users')
def users():
    return str(userData.toJSON()).replace("'","\"")
@app.route('/users/register/<id>/<pw>/<maxTime>/<location>', methods=['POST'])
def register(id,pw,maxTime,location):
    thing = {"id": int(id), "password": pw, "maxtime": int(maxTime), "location": location}
    userData.addToDb(thing)
    return thing



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=9090)