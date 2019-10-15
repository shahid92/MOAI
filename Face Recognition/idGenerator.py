import cv2

video_capture = cv2.VideoCapture(-1)
face_cascade = cv2.CascadeClassifier('faces.xml')

Id=int(input("ENTER ID NUMBER:"))
sampleNum=0
def detect(gray, frame):
   global sampleNum
   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x, y, w, h) in faces:
      cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
      sampleNum=sampleNum+1
      image_name="dataset/user_{0}.{1}.jpg".format(sampleNum,Id)
      print(image_name)
      cv2.imwrite(image_name,gray[y:y+h,x:x+w])
   return frame
   
while True:
   ret, frame = video_capture.read()
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   canvas = detect(gray, frame)
   cv2.imshow('Video', canvas)
   k=cv2.waitKey(10)
   if k==27:
      break
   elif sampleNum>50:
      break
      
video_capture.release()
cv2.destroyAllWindows()
