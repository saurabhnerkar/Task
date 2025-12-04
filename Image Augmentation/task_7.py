from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
import matplotlib.pyplot as plt
import numpy as np


gen = ImageDataGenerator(
    rotation_range=20,
    horizontal_flip=True,
    zoom_range=0.2
)


img = load_img("car_image.jpg")  
img_array = img_to_array(img)
img_array = img_array.reshape((1,) + img_array.shape)   


aug_iter = gen.flow(img_array, batch_size=1)

plt.figure(figsize=(8, 8))

for i in range(4):
    batch = next(aug_iter)
    image = batch[0] / 255.0

    plt.subplot(2, 2, i+1)
    plt.imshow(image)
    plt.axis('off')

plt.show()
