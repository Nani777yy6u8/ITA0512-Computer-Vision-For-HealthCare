#Perform Rotation of an image to clockwise and counter clockwise direction.

import cv2
import imutils 
image = cv2.imread(r"msd1.jpg") 
Rotated_image = imutils.rotate(image, angle=45) 
Rotated1_image = imutils.rotate(image, angle=90) 
cv2.imshow("Rotated", Rotated_image) 
cv2.imshow("Rotated1", Rotated1_image) 
cv2.waitKey(0) 
