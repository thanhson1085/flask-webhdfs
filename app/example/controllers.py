from flask import render_template
from app import app
from config import config as cfg
from flask import request, redirect, jsonify
from pywebhdfs.webhdfs import PyWebHdfsClient
from werkzeug import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
	
# upload a file to HDFS
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
            description: Return a successful message
        401:
            description: Unauthorized
        400:
            description: Bad Request
        500:
            description: Server Internal error
    """
    # hard-code config information. You should imporove it.
    hdfs = PyWebHdfsClient(host='webhdfs',port='50070', user_name='thanhson1085')
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            my_file = 'tmp/thanhson1085/data/' + filename
            hdfs.create_file(my_file, file)
            return jsonify({'success':'true'})

    return jsonify({'success':'false'})

# return allowed extensions
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
