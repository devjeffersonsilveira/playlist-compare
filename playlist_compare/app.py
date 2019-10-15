import os
import socket
import sys

import spotipy
from flask import Flask
from spotipy.oauth2 import SpotifyClientCredentials

from playlist_compare import list as listRoute, hello, search

app = Flask(__name__)


@app.route("/")
def helloRoute():
    return hello.hello()


@app.route("/list")
def lista():
    return listRoute.list()


@app.route("/search")
def searchRoute():
    return search.search()
