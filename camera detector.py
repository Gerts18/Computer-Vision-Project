from ultralytics import YOLO
import cv2

#Leer Modelo
model = YOLO("best.pt")

camara = cv2.VideoCapture(0)  # Toma la captura de la camara

while True:
    ret, frame = camara.read()  # Guarda un frame de la camara

    results = model.predict(frame, imgsz=640 )

    seg = results[0].plot()

    cv2.imshow("deteccion y segmentacion", seg)

    key = cv2.waitKey(1)
    if key == 27:
        break
camara.release()
cv2.destroyAllWindows()