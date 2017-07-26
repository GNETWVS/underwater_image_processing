#!/usr/bin/python2.7
# coding: utf-8

# pixelwise implementation of http://www.ipol.im/pub/art/2011/bcm_nlm/

# one letter variable names are associated with the very same variable in the linked research paper

# p and q defining pixels, they will be 1D 2-elements numpy array, describing their pixel coordinates

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

def compute_weights(rows, cols, dim, img):
    w = numpy.zeros((rows,cols))

    w[p,q] = 

def compute_euclidean_distance(p,q,f,img):
    for RGB_component in range(3):
        for lig in range(1,f+1):
            for col
