
import cv2

class View(object):

  def format(self, frame):
    encoded_frame = cv2.imencode('.jpg', frame)[1].tobytes()
    return (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + encoded_frame + b'\r\n')
