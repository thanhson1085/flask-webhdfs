from flask import render_template
from app import app
from config import config as cfg
import flask
from flask import request, redirect
from pywebhdfs.webhdfs import PyWebHdfsClient
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
@app.route('/index')
@app.route('/v1/upload', methods=['POST'])
def upload_file():
    """
    Upload file
    ---
    tags:
        - Files
    consumes: "multipart/form-data"
    parameters:
        -   name: file
            in: formData
            required: true
            paramType: body
            dataType: file
            type: file
    responses:
        200:
            description: Returns album_id after upload
        401:
            description: Unauthorized
        400:
            description: Bad Request
        500:
            description: Server Internal error
    """
    hdfs = PyWebHdfsClient(host='192.168.1.41',port='50070', user_name='thanhson1085')
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            my_file = 'tmp/thanhson1085/data/' + filename
            hdfs.create_file(my_file, file)
            return flask.jsonify({'success':'true'})

    return flask.jsonify({'success':'false'})

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
