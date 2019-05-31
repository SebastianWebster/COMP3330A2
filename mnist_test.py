#COMP3330 Assignment 2 Convolutional Neural network
#Sebastian Webster 31/5/2019
#Project Info and Dependancies
#Python Version = "3.5"
#Tensorflow Version = "2.0.0a0" (2.0.0 alpha 0)

from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


print("Train Images Dimensions:")
print(train_images.shape)
print("Training Labels:")
print(len(train_labels))

print("Test Images Dim:")
print(test_labels.shape)
print("Number of test labels:")
print(len(test_labels))

#Observe the data as it currently ranges from 0 - 255 grayscale pixel values
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

#This needs to be scaled down to a val between 0 and 1 for tensorflow

train_images = train_images / 255.0

test_images = test_images / 255.0

#Plot the first 25 images just to see if the data is right

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()


model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)


test_loss, test_acc = model.evaluate(test_images, test_labels)

print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images)




