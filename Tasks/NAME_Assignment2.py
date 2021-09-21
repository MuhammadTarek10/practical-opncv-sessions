import cv2
import numpy as np

def segment():
    """
        Required:
            make 2 modes, segmentation mode and normal mode
            normal mode is the normal camera without any changes
            segment mode is making a mask with specific colors (red, green, orange, blue)
            when the user click on a key from ['o', 'g', 'b', 'r'] the video feed itself
            is switched to only show that specific color on the video
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