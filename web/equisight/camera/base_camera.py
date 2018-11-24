
from threading import Thread, Lock, Event

class BaseCamera(Thread):
    '''Abstract class for the camera model'''
    mutex = Lock()
    _frame = None
    EMPTY_FRAME = bytes(0)

    def put(self, frame):
        with self.mutex:
            self._frame = frame

    def get(self):
        with self.mutex:
            frame = self._frame
        return frame

    def get_size(self):
        raise NotImplementedError('Calling base camera class')

    def __init__(self):
        Thread.__init__(self)
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        raise NotImplementedError('Calling base camera class')
