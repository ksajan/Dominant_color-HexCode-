from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np
import Finding_dominant_clors
from colormap import rgb2hex


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

plt.figure()
plt.axis("off")
plt.imshow(image)

array = [[41, 54, 38]]
for x in range(1,256):

    color = (image[x,256])
    
    if color!= array[0]:
        array.append(color)
    

print(array)


Shape = image.shape
print(Shape)

x,y,z = image.shape
array = []
lol = []
for i in range(3,x):

    if lol!= image[i-2, 256]:
        lol = image[i,256]
        array = array.append(lol)
        
print(array)
