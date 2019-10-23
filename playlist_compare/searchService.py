from flask import request


def search():
    token = request.args.get("token")
    username = request.args.get("username")
    spotify_instance = getSpotifyInstance(token)
    playlists = spotify_instance.user_playlists(username)

    return spotify_instance.search(q='artist:' + 'wazer', type='artist')
