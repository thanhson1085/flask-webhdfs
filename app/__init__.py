from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
from config import config as cfg

app = Flask(__name__, template_folder="../templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(cfg.MYSQL_USER, cfg.MYSQL_PASSWORD, cfg.MYSQL_HOST, cfg.MYSQL_DB)
db = SQLAlchemy(app)

from app.module_search import controllers
