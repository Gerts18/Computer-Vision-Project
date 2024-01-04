from ultralytics import YOLO
import cv2

#Leer Modelo entrrenado
model = YOLO('best.pt')

imagen = cv2.imread('test\Papayas_027.jpg') #Cargar imagen

while True:

    results = model.predict(imagen, imgsz=640 )

    seg = results[0].plot()

    cv2.imshow("Deteccion y Segmentacion", seg)

    cv2.imshow('imagen original',imagen)

    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()