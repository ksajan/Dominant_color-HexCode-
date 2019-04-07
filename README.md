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
  



  ### Result of eliminating neutral colors
   this little code snippet is an early stage of removing neutral color from dominat color histogram by changing number of clusters from the initial value by number of neutral color it contains.
   
   code snippet part of it
   ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/deleting%20particular%20color%20snippet.png " code snippet")
   
   ## Result:
   ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/Figure_3.png " result png file")



## Update:
I have updated the utills and finding_dominant_clors.py file with update KMeans algorith and removing particular pixel value from histogram while clustring all pixel value using initial given cluster value. this gives the most dominant color is being used as you can see from above result. this is only applicable only if you have the particular pixel RGB value with you( i have used the white and black pixel harcoded which is used in the original image ![alt text](https://github.com/ksajan/Dominant_color-HexCode-/blob/master/image/images.png " input image"). So as you can see it has removed the black and white RGB value from the histogram . this won't be in your case you have to find the the pixel value in you image for example [255,255,255] to [225, 225, 225] can be seen white and [0,0,0] and [2,2,2] both are black. So, please check the values before using the above script directly.
It will be next update so that we can remove the pixel values in a range so it can work for all image without worring about the particular pixel value and hardcoding it. Thanks Stay tuned for more amazing updates.
