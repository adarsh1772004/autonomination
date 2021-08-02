import cv2
image=cv2.imread("newImage.jpg")
window_name = 'Earth'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (600,750)
fontScale=1
color=(0,0,128)
thikness = 2
newImage=cv2.putText(image,'Earth', org, font, fontScale, color, thikness, cv2.LINE_AA)
cv2.imshow(window_name, newImage)
#cv2.imwrite("textImage.jpg", newImage)
cv2.waitKey(0)
