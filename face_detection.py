import numpy as np
import cv2
import serial
import time
import datetime
# Setting serial port to COM4 at bard rate of 9600
ser = serial.Serial('COM3',9600)
time.sleep(1)
face_cascade = cv2.CascadeClassifier('data\haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
while(True):
#capture frame by frame
# Read and record the data
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
    scaleFactor=1.5, minNeighbors=5)
#(WORK ON HOW TO USE MORE NO OF HARCASCADE AT SAME TIME)
    for (x,y,w,h) in faces:
        print(x,y,w,h)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        #Recognize? Deep learning model
        img_item = "my-image_new.png"
        cv2.imwrite(img_item, roi_gray)
        color = (255,0,0)
        stroke = 2
        k=cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)
        b = ser.readline() # read a byte string
        string_n = b.decode()
        string=string_n.rstrip()
        cv2.putText(k, string, (x, y-10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200,255,12), 2)
        time.sleep(0.4)
    if np.any(k)==True:
        print(string)
        #Display the frame
        cv2.imshow('Frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
#when done release the capture
cap.release()
cv2.destroyAllWindows()