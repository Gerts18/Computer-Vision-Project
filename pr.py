import cv2
import numpy as np 
import os
folder = 'name_folder'
images = os.listdir(folder) 
i=0
for img in images:
    img_path = folder + '/' + img
    imagen = cv2.imread(img_path)
    imagen = cv2.resize(imagen,(640,640))
    cv2.imwrite(f'Papaya original + {i}+.jpg',imagen)
    i+=1
    