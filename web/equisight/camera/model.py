
import importlib
from .view import View
from .screenshot import Screenshot

class CameraModel(object):
  '''Object for factory method of retreiving a camera model'''
  cameras_dict = {
      'opencv':   ['.opencv_camera',   'OpenCVCamera']
  }
  camera = None
  view = View()

  def get_cameras(self):
    return list(self.cameras_dict.keys())

  def register_camera(self, name, path, file_name):
    if name not in self.cameras_dict:
      self.cameras_dict[name] = [path, file_name]

  def set_camera(self, name):
    (module_name, this_class) = self.cameras_dict[name]
    module = importlib.import_module(module_name, 'equisight.camera')
    self.camera = getattr(module, this_class)()
    self.camera.setDaemon(True)
    self.camera.start()

  def get_frame(self):
    while True: 
      if self.camera:
        frame = self.camera.get()
      else:
        frame = self.camera.EMPTY_FRAME
      yield self.view.format(frame)

  def screenshot(self, directory, file_name):
    s = Screenshot(directory, file_name, self.camera.get())
    s.start()
