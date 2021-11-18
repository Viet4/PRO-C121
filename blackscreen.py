import numpy as np
import cv2

cap = cv2.VideoCapture(0) 
image = cv2.imread("background.jpg") 

while (cap.isOpened()):

    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 

    frame = np.flip(frame, axis=1)

    u_black = np.array([104,153,70])
    l_black = np.array([30,30,0])

    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    f = np.where(f==0, image, f)

    cv2.imshow("unmasked", frame) 
    cv2.imshow("masked", f) 

    # ASCII TABLE UNICODES (113 = "q") (27 = ESC)
    if cv2.waitKey(10) == 113 or cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destroyAllWindows()