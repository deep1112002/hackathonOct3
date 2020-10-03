from flask import *
import cv2
import numpy as np
from keras.models import load_model
import math
import subprocess
app=Flask(__name__)

@app.route('/')
def starting():
    return render_template('newHome.html')
@app.route('/newHome.html')
def start1():
    return render_template('newHome.html')
@app.route('/nexIndex.html')
def go():
    return render_template('nexIndex.html')


if __name__=='__main__':
    app.run(debug=True)