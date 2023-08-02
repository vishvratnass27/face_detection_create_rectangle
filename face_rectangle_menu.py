#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import matplotlib.pyplot as plt
import numpy

print("please choose one service:")
print("detecte face and show the rectangle on face")

print('''1.detecte the face and show th image
2.detecte the face and show the video
3.detecte the face and and show the video and crop the rectangle
    ''')

x=int(input("enter what do you want:"))
if x == 1:
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    facemodel=cv2.CascadeClassifier("myhaarcascade_frontalface_default.xml")
    myface=facemodel.detectMultiScale(frame)
    len(facemodel.detectMultiScale(frame))
    x1=myface[0][0]
    y1=myface[0][1]
    x2=myface[0][0] + myface[0][2]
    y2=myface[0][1] + myface[0][3]
    cv2.rectangle(frame,(x1,y1),(x2,y2),[0,255,0],5)

    cv2.imshow("my_photo", frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cap.release()
    
elif x == 2:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
    
        facemodel=cv2.CascadeClassifier("myhaarcascade_frontalface_default.xml")
        myface=facemodel.detectMultiScale(frame)
    #frame[0:250,0:230]=frame[100:350,220:450]
        if len(myface)==1:
            x1=myface[0][0]
            y1=myface[0][1]
            x2=myface[0][0] + myface[0][2]
            y2=myface[0][1] + myface[0][3]
            #frame[y1:y2]=frame[x1:x2]
            cv2.rectangle(frame,(x1,y1),(x2,y2),[0,255,0],5)
    
        cv2.imshow("my_photo", frame)
        if cv2.waitKey(10) == 13:
            break

    cv2.destroyAllWindows()
    cap.release()   
    
elif x == 3:
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
    
        facemodel = cv2.CascadeClassifier("myhaarcascade_frontalface_default.xml")
        myface = facemodel.detectMultiScale(frame)
    
        if len(myface) == 1:
            x1 = myface[0][0]
            y1 = myface[0][1]
            x2 = myface[0][0] + myface[0][2]
            y2 = myface[0][1] + myface[0][3]
        
        # Crop the face region
            face = frame[y1:y2, x1:x2]
        
        # Resize the face region to a fixed size (e.g., 200x200)
            face_resized = cv2.resize(face, (200, 200))
        
        # Place the cropped face in the right section of the image
            frame[10:210, 420:620] = face_resized
        
        # Draw a rectangle around the detected face in the original frame
            cv2.rectangle(frame, (x1, y1), (x2, y2), [0, 255, 0], 5)
    
        cv2.imshow("my_photo", frame)
    
        if cv2.waitKey(10) == 13:
            break

    cv2.destroyAllWindows()
    cap.release()


# In[ ]:




