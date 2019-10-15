import os
import socket
import sys

import spotipy
from flask import Flask, request
from spotipy.oauth2 import SpotifyClientCredentials
from playlist_compare.config import getSpotifyInstance


def list():
    token = request.args.get("token")
    username = request.args.get("username")
    spotify_instance = getSpotifyInstance(token)
    playlists = spotify_instance.user_playlists(username)

    return playlists

    row = ""
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            row += ("{\"num\":%4d, \"uri\":\"%s\", \"name\":\"%s\"}," %
                    (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = spotify_instance.next(playlists)
        else:
            playlists = None
    json = "{row}"
    return json.format(row=row)
