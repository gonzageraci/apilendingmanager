from flask import Flask, json, jsonify, request
import apiTools as api

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"response":"Succesfull"})

@app.route("/", methods=["GET"])
def index():
    return "Welcome to my new API"

@app.route("/yield-optimizer")
def yields():
    return jsonify({"Yield Optimizer":"All yields"})

@app.route("/autofarm/<string:blockchain>")
def autofarm(blockchain):
    return jsonify(api.getAutofarm(blockchain))

@app.route("/autofarm")
def autofarmfull():
    return(jsonify(api.getAutofarmFull()))

@app.route("/beefy")
def beefyFull():
    return(jsonify(api.getBeefyFull()))

@app.route("/beefy/<string:blockchain>")
def beefy(blockchain):
    return(jsonify(api.getBeefy(blockchain)))

@app.route("/swamp")
def swampFull():
    return jsonify(api.getSwampFull())

@app.route("/swamp/<string:blockchain>")
def swamp(blockchain):
    return jsonify({str(blockchain):api.getSwamp(blockchain)})

@app.route("/grim")
def grim():
    return jsonify(api.getGrim())

if __name__ == '__main__':
    app.run(debug=True, port=5000)