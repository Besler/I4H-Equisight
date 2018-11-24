from .base_camera import BaseCamera
import cv2
import time

class OpenCVCamera(BaseCamera):
    def open_camera(self):
        self.camera = cv2.VideoCapture(self.CV_CAMERA)
        print('OpenCVCamera: Opened camera on {}'.format(self.CV_CAMERA))
        print('OpenCVCamera: Camera is {}'.format('open' if self.camera.isOpened() else 'closed'))

    def __init__(self):
        super(OpenCVCamera,self).__init__()
        self.CV_CAMERA = 0
        self.open_camera()

    def __del__(self):
        super(OpenCVCamera, self).__init__()
        self.camera.release()

    def run(self):
        while not self.stopped():
            time.sleep(5.0/1000.0)
            if not self.camera.isOpened():
                self.put(self.EMPTY_FRAME)
                continue

            # read current frame
            _, img = self.camera.read()

            # encode as a jpg image and return it
            self.put(cv2.imencode('.jpg', img)[1].tobytes())

        # Done, close connection
        self.camera.release()
