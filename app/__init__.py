from flask import Flask, send_from_directory, jsonify
from config import config as cfg

app = Flask(__name__, static_url_path='')
Flask(__name__, template_folder="../swagger", static_folder="../swagger")

from app.example import controllers

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

from flask_swagger import swagger
# Swagger Doccument for API
@app.route('/docs')
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Files API"
    swag['basePath'] = "/"
    return jsonify(swag)

# Cross origin
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin','*')
    response.headers.add('Access-Control-Allow-Headers', "Authorization, Content-Type")
    response.headers.add('Access-Control-Expose-Headers', "Authorization")
    response.headers.add('Access-Control-Allow-Methods', "GET, POST, PUT, DELETE, OPTIONS")
    response.headers.add('Access-Control-Allow-Credentials', "true")
    response.headers.add('Access-Control-Max-Age', 60 * 60 * 24 * 20)
    return response
