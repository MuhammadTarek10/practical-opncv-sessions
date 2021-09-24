import cv2

def segment():
    """
        inputs:
            None
        outputs:
            show a camera feed with specific color filters
    """
    # FUNCTION FOR THE CALLBACK OF TRACKBARS
    def nothing(x):
        pass

    # TRACKBARS FOR CHANING HSV VALUES
    cv2.namedWindow('Bars')
    cv2.createTrackbar('HMin', 'Bars', 0, 179, nothing)
    cv2.createTrackbar('HMax', 'Bars', 179, 179, nothing)
    cv2.createTrackbar('VMin', 'Bars', 0, 255, nothing)
    cv2.createTrackbar('VMax', 'Bars', 255, 255, nothing)
    cv2.createTrackbar('SMin', 'Bars', 0, 255, nothing)
    cv2.createTrackbar('SMax', 'Bars', 255, 255, nothing)

    cap = cv2.VideoCapture(0)
    
    # HASH MAP TO GET LOWER AND UPPER VALUES OF HSV COLORS
    LOWER_COLORS = {'o': (0,70,130), 'y':(25, 100, 100),'g':(45,70,70), 'b': (100,100,0)}
    UPPER_COLORS = {'o': (10,255,255), 'y':(40,255,255), 'g':(100,255,255), 'b': (130,255,255)}

    s = False

    while True:
        ret, frame = cap.read()
        
        # IF ON SEGMENT MODE
        if s:
            filtered = cv2.GaussianBlur(frame, (5,5), 1) 
            hsv = cv2.cvtColor(filtered, cv2.COLOR_BGR2HSV)
            lower = (cv2.getTrackbarPos('HMin', 'Bars'),cv2.getTrackbarPos('SMin', 'Bars'),cv2.getTrackbarPos('VMin', 'Bars'))
            upper = (cv2.getTrackbarPos('HMax', 'Bars'),cv2.getTrackbarPos('SMax', 'Bars'),cv2.getTrackbarPos('VMax', 'Bars'))
            mask = cv2.inRange(hsv, lower, upper)
            frame[mask==0]=0
            # YOU ALSO CAN USE
            # frame = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('Camera', frame)

        k = cv2.waitKey(1)
        # TO AVOID chr(k) ERROR
        if k == -1:
            continue

        # SWITCH BETWEEN ON AND OFF MODE
        if chr(k) == 's':
            s = not s
        
        # GET VALUES OF SPECIFIC COLOR PRESSED ON THE KEYBOARD
        if chr(k) in 'ogby':
            l = LOWER_COLORS[chr(k)]
            u = UPPER_COLORS[chr(k)]
            cv2.setTrackbarPos('HMin', 'Bars', l[0])
            cv2.setTrackbarPos('SMin', 'Bars', l[1])
            cv2.setTrackbarPos('VMin', 'Bars', l[2])
            cv2.setTrackbarPos('HMax', 'Bars', u[0])
            cv2.setTrackbarPos('SMax', 'Bars', u[1])
            cv2.setTrackbarPos('VMax', 'Bars', u[2])

        if k == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()

segment()