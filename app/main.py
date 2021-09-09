from flask import Flask, request
from redis import Redis
import redis


app = Flask(__name__)
r = Redis(host='redis', decode_responses=True)


@app.route('/')
def home_view():
    if not r.get('counter'):
        r.set('counter', 0)
    r.incr('counter')
    return f"You are the {r.get('counter')} th user"


if __name__ == '__main__':
    app.run(debug=True)