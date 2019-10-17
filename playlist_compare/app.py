from flask import Flask, request, json

from playlist_compare import playlistService, helloService, searchService

app = Flask(__name__)


@app.route("/")
def helloRoute():
    data = helloService.hello()
    return json.jsonify(data)


@app.route("/list")
def listAll():
    token = request.args.get("token")
    username = request.args.get("username")

    data = playlistService.getAll(token, username)
    return json.jsonify(data)


@app.route("/listOne")
def listOne():
    token = request.args.get("token")
    username = request.args.get("username")
    playlist = request.args.get("playlist")

    data = playlistService.getTracks(token, username, playlist)
    return json.jsonify(data)


@app.route("/listDuplicates")
def listDuplicates():
    token = request.args.get("token")
    username = request.args.get("username")

    data = playlistService.getDuplicates(token, username)
    return json.jsonify(data)


@app.route("/search")
def searchRoute():
    data = searchService.search()
    return json.jsonify(data)
