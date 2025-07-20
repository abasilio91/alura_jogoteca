from flask import Flask

from databases.config import Config
from databases.db import db
import config

app = Flask(__name__)
app.secret_key=config.SECRET_KEY
app.config.from_object(Config)
db.init_app(app)
with app.app_context():
    db.create_all()

from views import *

if __name__ == '__main__':
    app.run(debug=True)