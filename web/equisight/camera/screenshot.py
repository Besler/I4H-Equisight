
from threading import Thread
import os
import cv2

class Screenshot(Thread):

  def __init__(self, directory, file_name, frame):
    Thread.__init__(self)
    self.daemon = True
    self._file_name = file_name
    self._frame = frame
    self._dir = directory

  def run(self):
    full_path = os.path.join(self._dir, self._file_name)
    if os.path.exists(full_path):
      print("Screenshot: File {} exists and will not overwrite".format(full_path))

    if self._file_name is None:
      print("Screenshot: Given empty file name.")

    if not os.path.isdir(self._dir):
      os.makedirs(self._dir)

    cv2.imwrite(full_path, self._frame)

    print("Screenshot: Wrote {}.".format(full_path))
