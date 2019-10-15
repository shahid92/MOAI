import cv2
import numpy as np

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "faces.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(1)
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
while True:
   ret, im =cam.read()
   gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
   faces=faceCascade.detectMultiScale(gray, 1.2,5)
   for(x,y,w,h) in faces:
      cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
      Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
      print("id:",Id)
      print("conf:",conf)
      if(conf<50):
         if Id==1:
            Id="shahid"
      else:
         Id="Unknown"
      cv2.putText(im,str(Id),(x,y+h),font,2,(0,0,0),2)
   cv2.imshow('im',im)
   k=cv2.waitKey(1)
   if k==27:
      break
cam.release()
cv2.destroyAllWindows()
