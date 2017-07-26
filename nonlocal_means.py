#!/usr/bin/python2.7
# coding: utf-8

# pixelwise implementation of http://www.ipol.im/pub/art/2011/bcm_nlm/

import numpy
import math
import PIL import Image


print('######### USER INPUT - IMAGE FILE NAME (without extension)  ##############')
choix_image = raw_input('-->')
print('######### IMAGE FILE EXTENSION ###########')
image_extension = raw_input('-->')

# using PIL Image to load .jpg as numpy array, what about .png ?
# -> should be okay http://pillow.readthedocs.io/en/3.4.x/handbook/image-file-formats.html

img = Image.open(choix_image + image_extension)

# if 2D shape, how is dim defined ???

rows, cols, dim = img.shape

print('########### input image shape ###############')
print(img.shape)

###############
### weights ###
###############

w = numpy.zeros((rows,cols))

w[p,q] = 
