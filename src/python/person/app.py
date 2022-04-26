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
    tMsg = msg.GetAllPersonRequest()

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.dispatchProcessInput(tMsg)
    return jsonify(response)

@app.route("/persons/", methods=["POST"])
def postPerson():
    payload = {} 

    person = obj.Person(**request.get_json())
    tMsg = msg.CreatePersonRequest(person=person)

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.dispatchProcessInput(tMsg)

    return jsonify(response)

# GET person with id
@app.route("/persons/<int:id>", methods=["GET"])
def getPerson(id):
    tMsg = msg.GetPersonRequest(id)

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.dispatchProcessInput(tMsg)
    return jsonify(response)

# PUT to update person with id
@app.route("/persons/<int:id>", methods=["PUT"])
def updatePerson(id):

    person = obj.Person(**request.get_json())
    tMsg = msg.UpdatePersonRequest(person=person)
    tMsg.id = id

    tService = Director.CreateBusinessService("Python.FlaskService")
    response = tService.dispatchProcessInput(tMsg)

    return jsonify(response)

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