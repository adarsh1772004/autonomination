import cv2
import numpy as np
image1=cv2.imread("img1.jpg")
image2=cv2.imread("img2.jpg")
weightedSum = cv2.addWeighted(image1, 0.5, image2,0.4, 0)
cv2. imshow("meargedImage",weightedSum)
cv2.imwrite("newImage.jpg",weightedSum)
cv2.waitKey(0)