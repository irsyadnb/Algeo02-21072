import cv2
import numpy as np
import time
#
headcc = cv2.CascadeClassifier(r'C:\Users\ASUS\Documents\TBAlgeo2\Algeo02-21072\haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_POS_FRAMES)

def video():
    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    head = headcc.detectMultiScale(frame, 1.2, 2, 0 , (20, 20), (40, 40))

    # print type(head)
    # print head
    # print head.shape
    # print ("Number of heads detected: " + str(head.shape[0]))

    if len(head) > 0:
        for (x, y, w, h) in head:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 1)

    # cv2.rectangle(frame, ((0,frame.shape[0] -25)),(270, frame.shape[0]), (255,255,255), -1)
    # cv2.putText(frame, "Number of head detected: " + str(head.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

    cv2.namedWindow('Camera',cv2.WINDOW_NORMAL)
    cv2.imshow('Camera',frame)


while(cap.isOpened()):
    video()
    cf = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
    cap.set(cv2.CAP_PROP_POS_FRAMES, cf+50)
    # cv2.setTrackbarPos("pos_trackbar", "Frame Grabber", 
    int(cap.get(cv2.CAP_PROP_FPS))
    time.sleep(2)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

# print (fps)
cap.release()
cv2.destroyAllWindows()