import cv2
import pytesseract
from PIL import Image
import os
import argparse

arg = argparse.ArgumentParser()
arg.add_argument('-i' , '--image' , required=True)
arg.add_argument('-p' , '--preprocess' , type = str , default='thresh')
args = vars(arg.parse_args())

img = cv2.imread(args['image'])
gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

if args['preprocess']=='thresh':
    gray = cv2.threshold(gray ,0 , 255 , cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
elif args['preprocess']=='blur':
    gray = cv2.medianBlur(gray , 3)

filename = '{}.png'.format(os.getpid())
cv2.imwrite(filename , gray)

text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)



# from transform import four_point_transform
# import cv2
# import numpy as np
# import imutils
# import argparse
# from skimage.filters import threshold_local
#
# ap = argparse.ArgumentParser()
# ap.add_argument('-i' , '--image' , required=True)
# args = vars(ap.parse_args())
#
# img = cv2.imread(args['image'])
# # img = cv2.resize(img , (2500,3200))
# original = img.copy()
# ratio = img.shape[0]/1500
# print('Shape',img.shape)
# img = imutils.resize(img, height=1500)
#
# gray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# gray = cv2.GaussianBlur(img,(5,5),0)
# edged = cv2.Canny(gray ,0,50)
# print(gray.shape)
# print(img.shape)
# print(edged.shape)
#
# cv2.imshow('Gray' , gray)
# cv2.imshow('Edged' , edged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# cnts = cv2.findContours(edged.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)
# cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
#
# for c in cnts:
#     peri = cv2.arcLength(c, True)
#     approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#     if len(approx) == 4:
#         screenCnt = approx
#         break
#
# print("STEP 2: Find contours of paper")
# cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 2)
# cv2.imshow("Outline", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# warped = four_point_transform(original, screenCnt.reshape(4, 2) *ratio)
# warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
# T = threshold_local(warped, 11, offset=10, method="gaussian")
# warped = (warped > T).astype("uint8") * 255
#
# print("STEP 3: Apply perspective transform")
# cv2.imshow("Original", imutils.resize(original, height=650))
# cv2.imshow("Scanned", imutils.resize(warped, height=650))
# cv2.waitKey(0)
# cv2.destroyAllWindows()


