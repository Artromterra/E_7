from flask import Flask
import os
from flask_mongoengine import MongoEngine
from flask_caching import Cache

app = Flask(__name__)
# REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
# MONGODB_HOST = os.environ.get('MONGODB_HOST', 'localhost')
app.config['MONGODB_DB'] = 'my_tumble_log'
app.config['MONGODB_HOST'] = 'localhost'
app.config['MONGODB_PORT'] = 27017
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379/0'})
# cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://{redis_host}:6379/0'.format(redis_host=REDIS_HOST)})
db = MongoEngine(app)

def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
	app.run()