import os 
import numpy as np
import cv2
from keras.preprocessing.image import ImageDataGenerator,load_img, img_to_array, array_to_img

#Propgrama que permite aplicar la data augmentation, tomando una serie de imagenes para aplicarles dif cambios
#Y asi tener un data set mas amplio 

folder = 'DATASET' #Direccion del folder donde estan las imagenes
images = os.listdir(folder) #Cargamos el folder
images_increased = 4 #Especificamos la cantidad de imagenes modificadas que queremos por imagen

dataGen = ImageDataGenerator(
    rotation_range= 30,
    zoom_range= 0.2,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True,
    vertical_flip=True,  
)  #Se establecen los parametros de las modificaciones que le queremos aplicar a la imagen
t=0

for img in images:  #Ciclo for para crear las nuevas imagenes por imagen 
    img_path = folder + '/' + img
    try:     
        picture = load_img(img_path)
        picture = cv2.resize(img_to_array(picture),(640,640),interpolation=cv2.INTER_AREA)
        x=picture/255
        x= np.expand_dims(x,axis=0)
        i=0
        for batch in dataGen.flow(x,batch_size=1,save_to_dir='o',save_format='.jpg',save_prefix=f'Papaya_{t}'): #Especificamos algunos parametros de salida de nuestas imagenes modificadas
                                                # Se especifica el directorio donde se guardaran las imagenes, el formato, etc
            i+=1                              
            if i > images_increased:
                break; 
        t+=1  
    except:
        print(f'Error con la imagen {img_path}')
        


"""
ancho,alto = 225,225

i=0
num_img = 0

for img in images:
    img_list = os.listdir(folder)
    
    img_path = folder + '/' + img
    
    imagen = load_img(img_path,target_size=[1])
    imagen = cv2.resize(img_to_array(imagen),(ancho,alto),interpolation=cv2.INTER_AREA)
    x=imagen/255
    x= np.expand_dims(x,axis=0)
    t = 1
    
    for salida in dataGen.flow(x,batch_size=1):
        a = img_to_array(salida[0])
        imgs = salida[0,:,:] *255
        imgFinal = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
        cv2.imwrite('ImgMod'+"/%i%i.jpg"%(i,t),imgFinal)
        t+=1
        
        num_img+=1
        if t > images_increased:
            break
    i+=1
print(f'Imagenes impresas {num_img}')
"""