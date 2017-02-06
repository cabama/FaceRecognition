import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

diccionario = {}
diccionario['carlos'] = 1
diccionario['bea'] = 2

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    print('imagePaths: {0}'.format(imagePaths))
    #create empth face list
    faceSamples=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image paths and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        nombre = os.path.basename(imagePath).split('_')[0]
        Id= diccionario[nombre]
        print("Nombre: {0}, id: {1}".format(nombre, Id))

        # extract the face from the training image sample
        faces=detector.detectMultiScale(imageNp)
        print('faces: {0}'.format(faces))
        #If a face is there then append that in the list as well as Id of it
        faceSamples.append(imageNp)
        Ids.append(Id)
    return faceSamples,Ids
faces,Ids = getImagesAndLabels('dataSet')
print faces
print('\n')
print Ids
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner/trainner2.yml')