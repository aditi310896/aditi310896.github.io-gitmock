import io
import torch
from PIL import Image
from keras import layers
from keras import models
from keras import optimizers
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array, load_img
from keras.models import load_model
import tensorflow as tf



def get_model():
	global model
	model = load_model('checkpoint_final.h5')
	print("Loaded Model from disk")
	model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
	return model