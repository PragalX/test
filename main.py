from flask import Flask, request, jsonify
from PragyanAPI import api

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'HELLO DEAR FIRAANDS'

@app.route("/chat-gpt", methods=["GET", "POST"])
def chat_gpt():
    if request.method == "GET":
        return jsonify({"_":"I ONLY ACCEPT POST REQUESTS"})
    elif request.method == "POST":
        json_ = request.json
        if not json_:
            return jsonify({"Error": "Something went wrong"})
        try:
            ask = json_["ask"]
            response = api.datagpt(ask)
            return jsonify(response)
        except KeyError:
            return jsonify({"Error": "Invalid Data"})
        except Exception as e:
            return jsonify({"Error": str(e)})
    else:
        return jsonify({"Error": "Method not Acceptable"})
