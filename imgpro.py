
import cv2
import numpy as np
import matplotlib.pyplot as plt



# 1.read the img
img=cv2.imread('C:/Users/hp/Desktop/img.png')
cv2.imshow("img",img)
cv2.waitKey(0)

#2. Change Color of Top-Right QuarterModify the top-right quarter of the image by changing its color using array slicing.
h,w,=img.shape[:2]
img1=img.copy()

img1[0:h//2,0:w//2]=0,0,255

cv2.imshow("img",img1)
cv2.waitKey(0)

#3. Brighten Bottom-Left Quarter ncrease brightness of the bottom left quarter of the image.

img3=img.copy()

r=np.float32(img3[h//2:,0:w//2])+1

c=255/np.log(1+np.max(r))
log_transformed=c*np.log(r)
r=np.uint8(log_transformed)
log_transformed=np.uint8(cv2.normalize(log_transformed,None,0,255,cv2.NORM_MINMAX))

img3[h//2:,0:w//2]=log_transformed

cv2.imshow("img",img3)
cv2.waitKey(0)

#4. Enhance the ImageApply an enhancement technique (e.g., histogram equalization, CLAHE). Explain why you chose it.

img4=img.copy()

gray = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))

enhanced_channel = clahe.apply(gray)

cv2.imshow('equalized', enhanced_channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

#5.Remove NoiseApply a suitable noise removal filter (e.g., Gaussian, Median). Justify your choice

img5=img.copy()

img5=cv2.medianBlur(img5,3)

cv2.imshow("img",img5)
cv2.waitKey(0)
##########################################################################

#6.Isolate specific objects (The most important objects from your opinion) fromthe image and make the rest black.

img6 =cv2.imread('C:/Users/hp/Desktop/img8.png')


h,w,_= img6.shape

for y in range(h):
    for x in range(w):
        p, g, r = img6[y, x]
        if p > 225 and g > 225 and r > 225:
            img6[y, x] = [0, 0, 0]  # نغيره لأسود

cv2.imshow("img",img6)
cv2.waitKey(0)


#####################################################
#7 Overlay a watermark image (e.g., logo) onto your image

img7=img.copy()

RR=cv2.imread('C:/Users/hp/Desktop/RR.png')

RR= cv2.resize(RR, (img.shape[1], img.shape[0]))

a = 0.3
b = 1 - a


output = cv2.addWeighted(img, b, RR, a, 0)

cv2.imshow("img",output)
cv2.waitKey(0)


#8 Foreground Extraction extract and display the foreground from the background.

img8 = cv2.imread('C:/Users/hp/Desktop/img8.png')
gray = cv2.cvtColor(img8, cv2.COLOR_BGR2GRAY)

h, w = gray.shape
result = img8.copy()

for y in range(h):
     for x in range(w):
          if gray[y, x] > 238:
                result[y, x] = [0, 0, 0]

cv2.imshow("Text Extracted", result)
cv2.waitKey(0)
cv2.destroyAllWindows()


#9-histo
h ,w=img.shape[:2]

H= h  // 3


part1 = img[0:H, :]
part2 = img[H:2*H, :]
part3 = img[2*H:h, :]


hsv1 = cv2.cvtColor(part1, cv2.COLOR_BGR2HSV)
gray2 = cv2.cvtColor(part2, cv2.COLOR_BGR2GRAY)
lab3 = cv2.cvtColor(part3, cv2.COLOR_BGR2LAB)


gray22 = cv2.cvtColor(gray2, cv2.COLOR_GRAY2BGR)



final = np.vstack((hsv1, gray22, lab3))

cv2.imshow(" the finally",final)
cv2.waitKey(0)







