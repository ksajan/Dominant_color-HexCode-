# Dominant_color-HexCode-
It extract the dominant color from image using opencv while eliminating neutral colors and provide with hexCode of those dominant color

## Approach

  we are going to use Kmeans implemented using sckit learn. We'll plot most dominant color using matplotlib. I used argparse to parse command line argument. the utils package contains two helper functions which take single parameter. The kmeans algorithm assigns each pixel in our image to the closest cluster. Now we create a histogram by using number cluster given using argparse --cluster.
  we define a 300*50 pixel rectanle to hold the most dominat colors in the image
  Now, we perform array computation to get the different values of RGB  and store it in array then using these array to find hex code using pypi library colormap using the below command.
  ```python
pip install colormap
```
  after converting to hex code we store these values in array print it.
  
  this code takes two argument one is image patth and cluster value
  if we increase thee value of cluster value the number of RGB value increase as cluster value
  
  ```python
  python Finding_dominant_clors.py --image 0.jpg --cluster 3
  ```
  
  input image:
  ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/1.jpg "input image")
  
  Histogram with cluster value = 3:
  ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/Figure_2.png "Histogram with cluster value = 3")
  
  Histogram with cluster value = 4:
  ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/3.png " Histogram with cluster value = 4")
  
  
  Your result will look like something like this image attached below
  
  Result:
  ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/result.png " Result")
  
  
  
