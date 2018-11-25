#!/usr/bin/env python
from flask import Flask, render_template, Response, request
from .camera.model import CameraModel
import os

app = Flask(__name__)
camera = CameraModel()
camera.set_camera(os.getenv('EQUISIGHT_CAMERA', 'opencv'))

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

@app.route('/screen_shot', methods=['POST'])
def screen_shot():
    if request.method == "POST":
        req_data = request.get_json(force=True)
        if 'file_name' in req_data:
            file_name = req_data['file_name']
            camera.screenshot(os.path.join(app.instance_path, 'images'), file_name)
    return 'Writing file {}\n'.format(file_name)
