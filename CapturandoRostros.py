import cv2
import os
import imutils

personName = 'Juan'
dataPath = 'C:/Users/juan velandia/Desktop/Reconocimiento facial/Data'
personPath = dataPath + '/' + personName
#print(personPath)
if not os.path.exists(personPath):
    print('Carpeta creada: ',personPath)
    os.makedirs(personPath)

cap = cv2.VideoCapture('Juan.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
count = 0
