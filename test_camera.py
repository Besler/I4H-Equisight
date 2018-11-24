
# Imports
import numpy as np
import cv2
import os

def camera_indicies():
    index = 0
    arr = []
    while True:
        cap = cv2.VideoCapture(index)
        if not cap.read()[0]:
            break
        else:
            arr.append(index)
        cap.release()
        index += 1
    return arr

dev = 1
cap = cv2.VideoCapture(dev)
if not cap.isOpened():
    os.sys.exit('ERROR: Cannot open camera {}'.format(dev))

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

