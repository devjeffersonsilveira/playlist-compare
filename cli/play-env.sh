#!bin/bash
export SPOTIPY_CLIENT_ID="8b5bf79b29194773b23a98c45eb96467"
export SPOTIPY_CLIENT_SECRET="4ce271b90c26454ab83557073f7c214d"
. cli/play-env.sh; FLASK_APP=playlist-compare/app.py FLASK_DEBUG=1 python -m flask run -h0.0.0.0 -p80
