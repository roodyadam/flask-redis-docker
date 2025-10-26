from flask import Flask
import redis
import os

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.environ.get('REDIS_HOST', 'redis'),
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():
    return '''
        <h1>Welcome to Flask + Redis Multi-Container App!</h1>
        <p>This is a simple Flask application using Redis as a database.</p>
        <p><a href="/count">Click here to visit the counter page</a></p>
    '''

@app.route('/count')
def count():
    try:
        visits = redis_client.incr('visit_count')
        return f'''
            <h1>Visit Counter</h1>
            <p>This page has been visited <strong>{visits}</strong> times.</p>
            <p><a href="/count">Refresh to increment</a> | <a href="/">Go back home</a></p>
        '''
    except redis.ConnectionError:
        return '''
            <h1>Error</h1>
            <p>Could not connect to Redis database.</p>
        ''', 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)