from flask import Flask
from app. config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os



app = Flask(__name__)

# configuration of csrf token
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf = CSRFProtect(app)
csrf.init_app(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import  routes, models
app.register_blueprint(routes.bp)

#if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=5000, debug=True)
