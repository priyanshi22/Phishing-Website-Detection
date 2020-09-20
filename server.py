import os
import prediction
import accuracy
from decimal import Decimal
from flask import Flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from flask import jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)

UPLOAD_FOLDER= '/files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','py'])
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/result')
def result():
    urlname  = request.args['name']
    pre  = prediction.getResult(urlname)
    accuracy.acc1()
    accuracy.acc2()
    before = accuracy.acc3()
    after = accuracy.acc4()
    a = Decimal(after)
    b = Decimal(before)
    inc=a-b
    result="This is a "+str(pre)+"."+"\n Accuracy changed by "+str(inc)+"%"+"\n Present accuracy is "+str(after)
    return result

@app.route('/', methods = ['GET', 'POST'])
def hello():
	return  render_template("getInput.html")




if __name__ == '__main__':
    app.run(debug=True)
