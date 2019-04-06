import numpy as np 
import cv2
import argparse

ap  = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])

image[:,:,3] = 0
cv2.imwrite("dontknow.jpg", image)
cv2.imshow("image",dontknow.jpg )
"""
print(image)

bound = [
    ([0,0,0], [100,100,100]),
    ([200,200,200], [256,256,256]),
    ([124,124,124], [198,198,198])
]

for (lower, upper) in bound:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.imwrite("download.jpg", image)
    cv2.waitKey(0)

"""