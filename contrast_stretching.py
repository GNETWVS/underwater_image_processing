#!/usr/bin/python2.7
# coding: utf-8

import cv2
import numpy as np


print('######### USER INPUT - IMAGE FILE NAME (without extension)  ##############')
choix_image = raw_input('-->')
print('######### IMAGE FILE EXTENSION ###########')
image_extension = raw_input('-->')

img = cv2.imread(choix_image + image_extension,-1)

cv2.imshow('image d\'origine',img)
cv2.waitKey(0)

nbLi, nbCol, dim = img.shape

img = cv2.imread(choix_image + image_extension,-1)
img = np.float32(img)

imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(imgYCrCb)

print('======= shape Y ==========')
print(y.shape)

cv2.imshow('luminance d\'origine',y/255)
cv2.waitKey(0)

print('=====composante y=====')
print(y)
print('=====composante cr====')
print(cr)
print('=====composante cb====')
print(cb)
                             
#######################################
#### TRY STRETCHING ON y COMPONENT ####
#######################################

maxiY = np.amax(y)
miniY = np.amin(y)

new_y = y #on initialise en copiant une variable de même format

if (maxiY < 255) or (miniY > 0):
	print('/!\ /!\ Stretching on y component realized')
	for li in range(nbLi):
		for col in range(nbCol):
			new_y[li,col] = round(( (y[li,col]-miniY)/(maxiY-miniY) ) * 255)
else:
	print('/!\/!\ No stretching on y component realized')

result_img = img #on initialise en copiant une variable de même format
result_img[:,:,0] = y
result_img[:,:,1] = cr
result_img[:,:,2] = cb

print(result_img.shape)
print('=====composante y=====')
print(result_img[:,:,0])
print('=====composante cr====')
print(result_img[:,:,1])
print('=====composante cb====')
print(result_img[:,:,2])

resultBGR = cv2.cvtColor(result_img, cv2.COLOR_YCrCb2BGR)

#print('======result_img array data type=======')
#print(np.ndarray.dtype(result_img))

cv2.imshow(resultBGR)
cv2.waitKey(0)
cv2.destroyAllWindows()
