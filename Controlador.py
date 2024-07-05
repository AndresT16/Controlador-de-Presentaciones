import cv2
import os
from cvzone.HandTrackingModule import HandDetector

#variables
width,height = 720,480
folderPath = "Presentacion"

#camara 
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#lista de imagenes
pathImagenes = os.listdir(folderPath)
print(pathImagenes)

#variables2
imgNumber = 0
hs, ws = 120,213

#detectar mano
detector = HandDetector(detectionCon=0.8,maxHands=1)


while True:
    #imagen
    sucess, img= cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath,pathImagenes[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands , img = detector.findHands(img, flipType=False)

    #Anadir camaraweb a las diapos
    imgSmall= cv2.resize(img,(ws,hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w-ws:w] = imgSmall

    cv2.imshow("Image", img)
    cv2.imshow("Presentaciones", imgCurrent)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break