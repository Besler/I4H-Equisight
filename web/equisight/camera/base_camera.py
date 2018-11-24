
from threading import Thread, Lock, Event

class BaseCamera(Thread):
    '''Abstract class for the camera model'''
    mutex = Lock()
    _frame = None
    EMPTY_FRAME = bytes(0)

    def put(self, frame):
        self.mutex.acquire()
        self._frame = frame
        self.mutex.release()

    def get(self):
        self.mutex.acquire()
        frame = self._frame
        self.mutex.release()
        return frame

    def __init__(self):
        Thread.__init__(self)
        self._stop_event = Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        raise NotImplementedError('Calling base camera class')
