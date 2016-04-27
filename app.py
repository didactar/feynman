from flask import Flask
from database import db
import config
from events.api import events

from flask.ext.cors import CORS

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(events)

CORS(app)

if __name__ == '__main__':
    app.run(threaded=True)
