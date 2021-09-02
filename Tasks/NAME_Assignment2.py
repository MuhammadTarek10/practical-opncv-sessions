import cv2
import numpy as np

def segment():
    """
        inputs:
            None
        outputs:
            show a camera feed with specific color filters
    """
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        
    
        cv2.imshow('Camera', frame)

        k = cv2.waitKey(1)
        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

segment()