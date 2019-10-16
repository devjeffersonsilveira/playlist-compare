from playlist_compare.config import getSpotifyInstance


def list(token=None, username=None):
    spotify_instance = getSpotifyInstance(token)
    playlists = spotify_instance.current_user_playlists(2)

    row = "["
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            row += ("{\"num\":%4d, \"uri\":\"%s\", \"name\":\"%s\"}," %
                    (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
        if playlists['next']:
            playlists = spotify_instance.next(playlists)
        else:
            playlists = None
    row += "]"

    return row


def listOne(token, username, playlist):
    spotify_instance = getSpotifyInstance(token)
    tracks = spotify_instance.user_playlist_tracks(
        username, playlist, "items(track(id,name,artists,album(id,name,release_date)))")

    return tracks
