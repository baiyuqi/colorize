from flask import Flask, request
from  colorize.reference import pb_colorizer as colorizer
import cv2
app = Flask(__name__)

@app.route('/')
def hello_world():
    images = request.files.getList()
    data = request.data  # empty in some cases
    img_str = cv2.imencode('.jpg', data)[1].tostring()
    return 'Hello World!'
@app.route('/colorize')
def colorise():
    data = request.data  # empty in some cases

    return 'Hello World!'
if __name__ == '__main__':
    app.run()