from flask import Flask, jsonify, request, make_response
from grongier.pex import Director

from interop import obj,msg


app = Flask(__name__)

# ----------------------------------------------------------------
### CRUD FOR Person
# ----------------------------------------------------------------

# GET Infos
@app.route("/", methods=["GET"])
def getInfo():
    info = {'version':'1.0.6'}
    return jsonify(info)

@app.route("/persons/", methods=["GET"])
def getAllPersons():
    msg = msg.GetAllPersonResquest()

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.dispatchProcessInput(msg)
    return jsonify(response)

@app.route("/persons/", methods=["POST"])
def postPerson():
    payload = {} 

    person = obj.Person(request.get_json())
    msg = msg.CreatePersonRequest(Person=person)

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.OnProcessInput(msg)


    return jsonify(payload)

# GET person with id
@app.route("/persons/<int:id>", methods=["GET"])
def getPerson(id):
    payload = {}
    return jsonify(payload)

# PUT to update person with id
@app.route("/persons/<int:id>", methods=["PUT"])
def updatePerson(id):

    payload = {
    }
    return jsonify(payload)

# DELETE person with id
@app.route("/persons/<int:id>", methods=["DELETE"])
def deletePerson(id):
    payload = {}  
    return jsonify(payload)


# ----------------------------------------------------------------
### MAIN PROGRAM
# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', port = "8081")