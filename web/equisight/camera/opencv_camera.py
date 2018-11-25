from .base_camera import BaseCamera
import cv2
import time
from threading import Lock
import numpy as np

class OpenCVCamera(BaseCamera):
    camera_mutex = Lock()
    
    def open_camera(self):
        with self.camera_mutex:
            self.camera = cv2.VideoCapture(self.CV_CAMERA)
            print('OpenCVCamera: Opened camera on {}'.format(self.CV_CAMERA))
            print('OpenCVCamera: Camera is {}'.format('open' if self.camera.isOpened() else 'closed'))
            self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
            self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1024)
            self.camera.set(cv2.CAP_PROP_FPS, 120)
        print('OpenCVCamera: Camera size {}'.format(self.get_size()))

    def close_camera(self):
        with self.camera_mutex:
            self.camera.release()

    def __init__(self):
        super(OpenCVCamera,self).__init__()
        self.CV_CAMERA = 0
        self.open_camera()

    def __del__(self):
        self.close_camera()

    def run(self):
        while not self.stopped() and self.camera.isOpened():
            with self.camera_mutex:
                # read current frame
                did_read, img = self.camera.read()

                # encode as a jpg image and return it
                if did_read:
                    self.put(img)

        # Done, close connection
        self.close_camera()
    
    def get_size(self):
        frame = (0,0)
        with self.camera_mutex:
            if not self.camera.isOpened():
                frame = (0,0)
            else:
                frame_width = self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)
                frame_height = self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
                frame = (frame_width, frame_height)
        return frame
