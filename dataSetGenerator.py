
'''
import cv2
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=raw_input('enter your id')
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        print('Estoy dentro')
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imshow('frame',img)
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
    #wait for 100 miliseconds 
    #if cv2.waitKey(100) & 0xFF == ord('q'):
    #    break
    # break if the sample number is morethan 20
    if sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()
'''


import numpy as np
import cv2

idd = raw_input('Introduzca el ID del usuario: ')
muestraInt = 0
detector= cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    if(len(faces)!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imwrite("dataSet/"+idd +'_'+ str(muestraInt) + ".jpg", gray[y:y+h,x:x+w])
            muestraInt+=1


    cv2.imshow('frame',img)

    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif muestraInt>20:
        break
    
cap.release()
cv2.destroyAllWindows()