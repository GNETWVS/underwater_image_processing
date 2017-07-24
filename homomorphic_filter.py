#!/usr/bin/python2.7
# coding: utf-8

import cv2
import numpy as np
import matplotlib.pyplot as plt

print('######### USER INPUT - IMAGE FILE NAME (without extension)  ##############')
choix_image = raw_input('-->')
print('######### IMAGE FILE EXTENSION ###########')
image_extension = raw_input('-->')

img = cv2.imread(choix_image + image_extension,-1)
img = np.float32(img)
img = img/255

#print('=============Résultat normalisation et float32')
#print(img.shape)
#print('----------------------------------')
#print(img)

cv2.imshow('visu normalise',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

rows,cols,dim=img.shape

rh, rl, cutoff = 2.5,0.5,32

imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
y,cr,cb = cv2.split(imgYCrCb)
print('=============Résultat luminance')
print(y.shape)
print('----------------------------')
print(y)

#np.savetxt('luminance',y)

cv2.imshow('visu luminance',y)
cv2.imwrite(choix_image+'.png',y*255)
cv2.waitKey(0)
cv2.destroyAllWindows()

y_log = np.log(y+0.01)

print('=============Résultat log')
print(y_log.shape)
print('--------------------------')
print(y_log)

y_fft = np.fft.fft2(y_log)
print('=============Résultat fft2')
print(y_fft.shape)
print('--------------------------')
print(y_fft)

y_fft_shift = np.fft.fftshift(y_fft)


DX = cols/cutoff
G = np.ones((rows,cols))
for i in range(rows):
    for j in range(cols):
        G[i][j]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl
        #G[i][j][1]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl

print('=====================matrice filtrage G')
print(G.shape)
print('--------------------------------------')
print(G)

# ordre du produit ? par important si produit element wise

#result_filter = np.multiply(y_fft_shift,G)
result_filter = G * y_fft_shift
print('======================Résultat filtre')
print(result_filter.shape)
print('----------------------------')
print(result_filter)

#result_interm = np.real(cv2.idft(np.fft.ifftshift(result_filter)))
result_interm = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter)))

#################################
### OVERFLOW SOURCE BELOW #######
#################################

result = np.exp(result_interm)
print('===========Résultat exponentiel')
print(result.shape)
print('-------------------------------')
print(result)

#np.savetxt('resultat',result)

print('==========Vérification dimension composantes================')
print('shape result:',result.shape)
print('shape cr:    ',cr.shape)
print('shape cb:    ',cb.shape)

#result_full = cv2.merge((result,cr,cb))

result_full = img
result_full[:,:,0] = result
result_full[:,:,1] = cr
result_full[:,:,2] = cb

resultRGB = cv2.cvtColor(result_full, cv2.COLOR_YCrCb2RGB)
resultBGR = cv2.cvtColor(result_full, cv2.COLOR_YCrCb2BGR)

#resultRGB = resultRGB*255
#resultBGR = resultBGR*255

# because cv2.imshow() denormalizes itself the images it's asked to show us
# but we then need to *255 the resultBGR before cv2.imwrite()

cv2.imshow('resultat',result)
cv2.imwrite('resultat_'+choix_image+'.png',result*255)
cv2.waitKey(0)
cv2.imshow('resultat RGB',resultRGB)
cv2.waitKey(0)
cv2.imshow('resultat BGR',resultBGR)
cv2.imwrite(choix_image + '_filtre_homo.png',resultBGR*255)
# il apparait que result BGR est 'le bon' resultat en termes de format d'image RGB
cv2.waitKey(0)
cv2.destroyAllWindows()

img_initiale = cv2.imread(choix_image + image_extension,-1)
img_resultat = cv2.imread(choix_image + '_filtre_homo.png',-1)

difference = np.absolute(np.subtract(img_initiale,img_resultat))
max_difference = np.amax(difference)

print('=====================Différence initiale/filtrée====================')
print(difference)
print('=====================numpy.amax(difference)=========================')
print(max_difference)
