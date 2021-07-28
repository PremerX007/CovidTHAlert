import cv2
img = cv2.imread("name.png")
x=140
y=244
h=110
w=320

x1=697
y1=245
h1=95
w1=245
crop_img = img[y:y+h, x:x+w]
crop_img2 = img[y1:y1+h1, x1:x1+w1]
cv2.imshow('1',crop_img)
cv2.imshow('2',crop_img2)
cv2.waitKey(0)