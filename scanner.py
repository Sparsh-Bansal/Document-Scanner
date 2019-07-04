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
# def document_scanner(original_image,height ,th1,th2 ):
#     global original
#     original = original_image.copy()
#     ratio = img.shape[0] /height
#     original_image = imutils.resize(original_image, height=height)
#     gray = cv2.cvtColor(original_image , cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray,(5,5),0)
#     edged = cv2.Canny(original_image,th1,th2)
#     print(gray.shape)
#     print(img.shape)
#     print(edged.shape)
#
#     cv2.imshow('Gray' , gray)
#     cv2.imshow('Edged' , edged)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     cnts = cv2.findContours(edged.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#     cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
#
#     for c in cnts:
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.02 * peri, True)
#
#         if len(approx) == 4:
#             screenCnt = approx
#             break
#     print("STEP 2: Find contours of paper")
#     cv2.drawContours(original_image, [screenCnt], -1, (0, 255, 0), 2)
#     cv2.imshow("Outline", original_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
#     warped = four_point_transform(original, screenCnt.reshape(4, 2) *ratio)
#     warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
#     T = threshold_local(warped, 11, offset=10, method="gaussian")
#     warped = (warped > T).astype("uint8") * 255
#     return warped
#
# img = cv2.imread(args['image'])
# print('Shape',img.shape)
# print(img.shape[0])
#
# if img.shape[1]>3000:
#     warped = document_scanner(img,1500,0,50)
# elif img.shape[1]<=3000:
#     warped = document_scanner(img,500,0,50)
#
#
#
# print("STEP 3: Apply perspective transform")
# cv2.imshow("Original", imutils.resize(original, height=650))
# cv2.imshow("Scanned", imutils.resize(warped, height=650))
# cv2.waitKey(0)
#


from transform import four_point_transform
import cv2
import numpy as np
import imutils
import argparse
from skimage.filters import threshold_local

ap = argparse.ArgumentParser()
ap.add_argument('-i' , '--image' , required=True)
args = vars(ap.parse_args())

def thresholding(img):
    dilated_img = cv2.dilate(img, np.ones((7, 7), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(img, bg_img)
    norm_img = diff_img.copy()  # Needed for 3.x compatibility
    cv2.normalize(diff_img, norm_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    _, thr_img = cv2.threshold(norm_img, 230, 0, cv2.THRESH_TRUNC)
    cv2.normalize(thr_img, thr_img, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    return thr_img


def document_scanner(original_image,heights):
    global original
    original = original_image.copy()
    for height in heights:

        ratio = img.shape[0] /height
        original_image = imutils.resize(original_image, height=height)
        gray = cv2.cvtColor(original_image , cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray,(5,5),0)
        _, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # gray = thresholding(original_image)
        cv2.imshow('Gray2',gray)

        print('Height',height)
        threshold = [0,50,100]
        for i in threshold:
            edged = cv2.Canny(original_image,i,i+50)
            print('{}  {}'.format(i,i+50))
        # print(gray.shape)
        # print(img.shape)
        #     print(edged.shape)

        # cv2.imshow('Gray' , gray)
            cv2.imshow('Edged' , edged)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

            cnts = cv2.findContours(edged.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
            cnts = imutils.grab_contours(cnts)
            cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
            check =False

            for c in cnts:
                peri = cv2.arcLength(c, True)
                approx = cv2.approxPolyDP(c, 0.02 * peri, True)

                if len(approx) == 4:
                    screenCnt = approx
                    check = True
                    break
            if check:
                print("STEP 2: Find contours of paper")
                cv2.drawContours(original_image, [screenCnt], -1, (0, 255, 0), 2)
                cv2.imshow("Outline", original_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                continue
        if check:
            break
        else:
            continue


    warped = four_point_transform(original, screenCnt.reshape(4, 2) *ratio)
    warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
    # _,warped = cv2.threshold(warped , 0 , 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imshow('YOY',warped)
    T = threshold_local(warped, 11, offset=10, method="gaussian")
    warped = (warped > T).astype("uint8") * 255
    return warped

img = cv2.imread(args['image'])
print('Shape',img.shape)
# print(img.shape[0])

# img = cv2.resize(img, (4000, 3000))
print(img.shape)
try:
    if img.shape[1]>3000:
        warped = document_scanner(img,[1500,1300])
    elif img.shape[1]<=3000:
        warped = document_scanner(img,[500,700,1200])
except:
    print("Image Not Captured Properly")
    warped = img



print("STEP 3: Apply perspective transform")
cv2.imshow("Original", imutils.resize(original, height=650))
cv2.imshow("Scanned", imutils.resize(warped, height=650))
cv2.waitKey(0)