#!/usr/bin/env python
from flask import Flask, render_template, Response
from .camera.model import CameraModel

app = Flask(__name__)
camera = CameraModel()
camera.set_camera('opencv')

# Load default config and override config from an environment variable
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='apples'
))
app.config.from_envvar('EQUISIGHT_SETTINGS', silent=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    f = camera.get_frame()
    return Response(f, mimetype='multipart/x-mixed-replace; boundary=frame')
