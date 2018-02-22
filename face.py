
import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
videocapture=cv2.VideoCapture(0)
while 1:
    ret, pic = videocapture.read()
    
    faces=face_cascade.detectMultiScale(pic,10,5)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(pic,(x, y),(x + w, y + h), (255,255, 0), 2)
    print "number of faces found:",format(len(faces))
    cv2.imshow("face",pic)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
videocapture.release()
cv2.destroyAllWindows()	
