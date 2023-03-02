from flask import Flask, jsonify, request
from grongier.pex import Director
from msg import Priority

import iris

app = Flask(__name__)

# ----------------------------------------------------------------
### CRUD FOR Person
# ----------------------------------------------------------------

# GET Infos
@app.route("/", methods=["GET"])
def get_info():
    """
    It returns a JSON object with a single key-value pair
    :return: A JSON object with the version number of the API.
    """
    info = {'version':'1.0.6'}
    return jsonify(info)

# DELETE person with id
@app.route("/bench/<int:id>", methods=["GET"])
def bench(id):

    msg = Priority(value=id)

    # service = Director.create_business_service("Python.BenchService")
    # response = service.ProcessInput(msg)
    service = Director.create_business_service("ObjectScript.BS")
    response = service.ProcessInput(iris.cls("Ens.StringRequest")._New(msg.value))

    return jsonify(response)


# ----------------------------------------------------------------
### MAIN PROGRAM
# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', port = "8080")