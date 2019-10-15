import os
import socket
import sys

import spotipy
from flask import Flask, request
from spotipy.oauth2 import SpotifyClientCredentials
from playlist_compare.config import getSpotifyInstance


def search():
    token = request.args.get("token")
    username = request.args.get("username")
    spotify_instance = getSpotifyInstance(token)
    playlists = spotify_instance.user_playlists(username)

    row = spotify_instance.search(q='artist:' + 'wazer', type='artist')

    json = "{row}"
    return json.format(row=row)
