from keras import layers
from keras import models
import numpy as np
from keras import optimizers
from commons import get_model
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
from PIL import Image
import io
import torchvision.transforms as transforms
import cv2



def read_image(file_path):
    print("[INFO] loading and preprocessing image...")
    #print(file_path)
    bulbimage = np.array(Image.open(io.BytesIO(file_path)))
    bulbimage = cv2.resize(bulbimage, dsize=(400, 400))
    
    #print(bulbimage)
    #my_transforms = transforms.Compose([transforms.Resize(400)])
    #bulbimage=my_transforms(bulbimage)
    #print(bulbimage)
    #bulbimage= load_img(file_path, target_size=(400, 400))  
    #bulbimage = img_to_array(bulbimage)
    bulbimage = bulbimage.astype('float') 
    #bulbimage= np.array(bulbimage).copy() 
    bulbimage = np.expand_dims(bulbimage, axis=0)
    bulbimage /= 255.
    print(bulbimage)
    return bulbimage

model=get_model()
import time
def test_single_image(path):
    bulbs = ['A19', 'BR2040', 'MR16', 'PAR203038', 'R20', 'T5T8']
    images = read_image(path)
    time.sleep(.5)
    preds = model.predict(images)  
    predictions = {
        "A19":round(preds[0][0],2),
        "BR2040":round(preds[0][1],2),
        "MR16":round(preds[0][2],2),
        "PAR203038":round(preds[0][3],2),
        "R20":round(preds[0][4],2),
        "T5T8":round(preds[0][5],2),}
	
    #predictions={
	#for idx, bulb, x in zip(range(0,6), bulbs , preds[0]):
        #print("ID: {}, Label: {} {}%".format(idx, bulb, round(x*100,2) ))}
    print('Final Decision:')
    time.sleep(.5)
    for x in range(3):
        print('.'*(x+1))
        time.sleep(.2)
    class_predicted = model.predict_classes(images)
    #class_predicted.shape()
    class_dictionary= {'A19': 0, 'BR2040': 1, 'MR16': 2, 'PAR203038': 3, 'R20': 4, 'T5T8': 5} 
    inv_map = {v: k for k, v in class_dictionary.items()} 
    result= inv_map[class_predicted[0]]
    #print("ID: {}, Label: {}".format(class_predicted[0], inv_map[class_predicted[0]]))  
    return predictions,result