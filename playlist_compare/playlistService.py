from playlist_compare.spotipyManager import SpotipyManager


def getAll(token: str, username: str):
    manager = SpotipyManager(token)
    playlists = manager.user_playlists(username)

    row = []
    while playlists:
        for playlist in playlists['items']:
            row.append(playlist)
        if playlists['next']:
            print("getting next page of playlists: " + playlists['next'])
            playlists = manager.next(playlists)
            continue
        playlists = None
    return row


def getTracks(token: str, username: str, playlist: str) -> list:
    manager = SpotipyManager(token)
    return manager.user_playlist_tracks(username, playlist)
    tracks = manager.user_playlist_tracks(username, playlist)

    row = []
    while tracks:
        for track in tracks['items']:
            row.append(track)
        if tracks['next']:
            print("getting next page of tracks: " + tracks['next'])
            tracks = manager.next(tracks)
            continue
        tracks = None

    return row


def getDuplicates(token: str, username: str):
    playlists = getAll(token, username)
    row = []
    for playlist in playlists:
        if playlist['owner']['id'] != username:
            continue

        print("checking tracks of: " + playlist['name'])
        tracks = getTracks(token, username, playlist['id'])
        unique = set()
        duplicate = set()
        for track in tracks:
            if track['track']['id'] in unique:
                duplicate.add(track['track']['id'])
                continue
            unique.add(track['track']['id'])
        if len(duplicate):
            row.append({
                'id': playlist['id'],
                'name': playlist['name'],
                'duplicates': list(duplicate)
            })

    return row
