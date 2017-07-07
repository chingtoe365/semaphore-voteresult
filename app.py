from flask import Flask, render_template, request, make_response, g
from redis import Redis
import os
import socket
import random
import json

app = Flask(__name__)

def get_redis():
    if not hasattr(g, 'redis'):
        g.redis = Redis(host="redis", db=0, socket_timeout=5)
    return g.redis

@app.route("/", methods=['POST','GET'])
def hello():
    redis = get_redis()
    # raw_data = json.dumps(redis.get('votes'))
    raw_data = json.dumps(redis.lrange('votes', 0, -1))
    # redis.set('foo', 'bar')
    # raw_data = json.dumps(redis.get('foo'))
    resp = make_response(render_template(
        'index.html',
        raw_data=raw_data
    ))
    return resp

# @app.route("/", methods=['POST','GET'])
# def hello():
#     # redis = get_redis()
#     # raw_data = json.dumps(redis.get('votes'))
#     resp = make_response(render_template(
#         'index.html',
#         # raw_data=raw_data
#     ))
#     return resp


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True)
