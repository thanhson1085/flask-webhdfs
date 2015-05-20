from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import jinja2
from config import config as cfg

app = Flask(__name__, template_folder="../templates")

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://{}:{}@{}/{}".format(cfg.MYSQL_USER, cfg.MYSQL_PASSWORD, cfg.MYSQL_HOST, cfg.MYSQL_DB)
db = SQLAlchemy(app)

# initial log application
if cfg.DEBUG:
    from logging import Formatter
    import logging
    file_handler = logging.FileHandler(cfg.LOG_FILE)
    if cfg.LOG_LEVEL not in [0, 10, 20, 30, 40, 50]:
        file_handler.setLevel(0)
    else:
        file_handler.setLevel(cfg.LOG_LEVEL)
    file_handler.setFormatter(Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(file_handler)

# initial a module
from app.module_search import controllers

# initial blueprint
app.register_blueprint(controllers.search, url_prefix='/search')
