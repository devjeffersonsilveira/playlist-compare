from spotipy import Spotify, util
from redis import Redis, RedisError
import json
import pprint


class SpotipyManager(Spotify):

    def __init__(
            self, auth=None, requests_session=True,
            client_credentials_manager=None, proxies=None, requests_timeout=None
    ):
        self.redis = Redis(host="127.0.0.1", db=0, port=6379)
        if self.redis.ping() == False:
            raise EnvironmentError
        self.redis.set("caca", 122)

        # super().__init__(
        #     auth, requests_session,
        #     client_credentials_manager, proxies, requests_timeout
        # )

    def user_playlist_tracks(self, user, playlist_id=None, fields=None,
                             limit=100, offset=0, market=None):
        tracks = self.redis.lrange("playlist:%s:tracks" % playlist_id, 0, -1)
        if tracks:
            return tracks
        print("passou")
        # playlists = super().user_playlist_tracks(
        #     user, playlist_id, fields, limit, offset, market)
        with open('playlist_compare/samples/tracks.json') as json_data:
            tracks = json.load(json_data)
        tracksId = []
        for item in tracks['items']:
            self.redis.rpush("playlist:%s:tracks" %
                             playlist_id, item['track']['id'])
            tracksId.append(item['track']['id'])

        return tracksId

    def user_playlists(self, user, limit=50, offset=0):
        self.redis.set("caca", 155)
        # playlists = self.redis.get("user")
        # if playlists:
        #     return playlists
        # playlists = super().user_playlists(user, limit, offset)
        with open('playlist_compare/samples/playlist.json') as json_data:
            playlists = json.load(json_data)

        # self.redis.set("user", user)

        return playlists

    # def next(self, any):
    #     with open('playlist_compare/samples/playlist_next.json') as json_data:
    #         d = json.load(json_data)
    #     return d

    def getAll(self, any):
        with open('playlist_compare/samples/playlist_items.json') as json_data:
            d = json.load(json_data)
        return d
