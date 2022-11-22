
# import the opencv library
import cv2
import pyautogui
import numpy as np
import pygetwindow
from PIL import Image
#
def realltime():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    
    while(True):
        
        # Capture the video frame
        # by frame

        ret, frame = vid.read()
        # Display the resulting frame
        cv2.imshow('FR', frame)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if  cv2.waitKey(1) & 0xFF == ord('q'):break
        if  cv2.waitKey(1) & 0xFF == ord('a'):
            cv2.imwrite('riltime.jpg', frame)
            
            
            
            # img1.set(myScreenshot)
            # im = Image.open(f'{img1.get()}')
            # im = im.crop((left+10,top-10,right-10,bottom-10))
            # im.save(img1.get())
            # img_foto1=Image.open(img1.get()).resize(500,500)
            # img_fototemp=ImageTk.PhotoImage(img_foto1)
            # img_label.configure(image=img_fototemp)
            # img_label.image=img_fototemp
            
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    
realltime()