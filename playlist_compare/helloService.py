from flask import request


def hello():
    return request.args.get("access_token")
