from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import numpy as np
from colormap import rgb2hex
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())
 
# load the image and convert it from BGR to RGB so that
# we can dispaly it with matplotlib
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
# show our image
plt.figure()
plt.axis("off")
plt.imshow(image)

# reshape the image to be a list of pixels
image = image.reshape((image.shape[0] * image.shape[1], 3))

# cluster the pixel intensities
clt = KMeans(n_clusters = args["clusters"])
clt.fit(image)
#print(clt)
# build a histogram of clusters and then create a figure
# representing the number of pixels labeled to each color
hist = utils.centroid_histogram(clt)
bar = utils.plot_colors(hist, clt.cluster_centers_)
#print(hist)

"""
array = []
#c = 0
for i in range(len(bar)):
    if bar[i] not in array:
 #       c+=1
        array.append(i)
print(bar)

"""

    
array = ([bar[0:1:1][0][255]])
#print(array)

c = 0
array1 = (bar[0:1:1][0])
    



for i in range(len(array1)-2):
    if np.array_equiv(array1[i], array[c]) == False:
        array.append(bar[0:1:1][0][i])
        c += 1

arr =np.array(array)
RGB = arr[:3]

HexCode = []
for i in range(len(RGB)):
    lol = RGB[i]
    HexCode.append(rgb2hex(lol[0],lol[1],lol[2]))
    
print(HexCode)


#for i in range(len)
"""
file = open("array.txt", 'wb')
file.write(bar)
file.close()
"""

# show our color bart
plt.figure()
plt.axis("off")
plt.imshow(bar)
plt.show()

