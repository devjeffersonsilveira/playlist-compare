import spotipy
import spotipy.util as util


def getSpotifyInstance(token=None, username=None, scopes=None):
    if scopes:
        token = util.prompt_for_user_token(username, scopes)
    if token:
        return spotipy.Spotify(auth=token, requests_timeout=1)

    return spotipy.Spotify()
