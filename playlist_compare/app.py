from flask import Flask, request, json

from playlist_compare import listService, helloService, searchService

app = Flask(__name__)


@app.route("/")
def helloRoute():
    data = helloService.hello()
    return json.jsonify(data)


@app.route("/list")
def listAll():
    token = request.args.get("token")
    username = request.args.get("username")

    data = listService.list(token, username)
    return json.jsonify(data)


@app.route("/listOne")
def listOne():
    token = request.args.get("token")
    username = request.args.get("username")
    playlist = request.args.get("playlist")

    data = listService.listOne(token, username, playlist)


@app.route("/search")
def searchRoute():
    data = searchService.search()
    return json.jsonify(data)
