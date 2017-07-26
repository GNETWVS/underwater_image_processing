#!/usr/bin/python2.7
# coding: utf-8

# pixelwise implementation of http://www.ipol.im/pub/art/2011/bcm_nlm/

# one letter variable names are associated with the very same variable in the linked research paper

# p and q defining pixels, they will be 1D 2-elements numpy array, describing their pixel coordinates

# in a first implementation, sigma and h won't be mathematically linked

# i and j loop indexes are only used when the loop goes through an image patch

###########################################################################################
##################### INITIALIZATION and FILTER PARAMETERS ################################
###########################################################################################

import numpy
import math
import PIL import Image


print('######### USER INPUT - IMAGE FILE NAME (without extension)  ##############')
choix_image = raw_input('-->')
print('######### IMAGE FILE EXTENSION ###########')
image_extension = raw_input('-->')

sigma, h, r, f = ### ?????????????? ###

# using PIL Image to load .jpg as numpy array, what about .png ?
# -> should be okay http://pillow.readthedocs.io/en/3.4.x/handbook/image-file-formats.html

img = Image.open(choix_image + image_extension)

# if 2D shape, how is dim defined ???

rows, cols, dim = img.shape

print('########### input image shape ###############')
print(img.shape)

##########################################################################################
############################# AUXILIARY FUNCTIONS ########################################
##########################################################################################

def compute_total_weight(p, rows, cols, dim, img, sigma, h, r, f):
    
    total_weight = 0

    for i in range(1,r+1):
        for j in range(1,r+1):
            q = numpy.array( [p[0]+i , p[1]+j] )
            total_weight += compute_weights(p, q, f, rows, cols, dim, img, sigma, h)
            q = numpy.array( [p[0]-i , p[1]-j] )
            total_weight += compute_weights(p, q, f, rows, cols, dim, img, sigma, h)
    return( total_weight )

##########################################################################################

# let's compute the exponential kernel weights

def compute_weights(p, q, f, rows, cols, dim, img, sigma, h):
    
    w = numpy.zeros((rows,cols))

    sigma2 = sigma**2
    
    d2 = compute_squared_euclidean_distance(p, q, f, img)
    
    return(math.exp( (-max(d2-2*sigma2,0.0) / h**2) ))

##########################################################################################

def compute_squared_euclidean_distance(p,q,f,img):
    
    sum_of_pixels_diff = 0

    # we consider every pixel in the patch but the one for which we're computing a new value

    for RGB_component in range(3):
        for i in range(1,f+1):
            for j in range(1,f+1):
                sum_of_pixels_diff += ( img[p[0]+i , p[1]+j] - img[q[0]+i , q[1]+j] )**2
    
    weight_for_mean = 3*((2*f+1)**2)
    
    return( sum_of_pixels_diff / weight_for_mean )
                
##########################################################################################

def sum_of_weighed_pixels(p, rows, cols, img, r):
    
    incremented_sum = 0

    for RGB_component in range(3):

    for i in range(1,r+1):
        for j in range(1,r+1):
            
            q = numpy.array( [p[0]+i , p[1]+j] )
            incremented_sum += img

##########################################################################################
########################### MAIN LOOP ####################################################
##########################################################################################

for row in range(rows):
    for col in range(cols):
        
        p = numpy.array( [row,col] )
        
        total_weight = compute_total_weight(p, rows, cols, dim, img, sigma, h, r, f)
        
        weighed_pixels_sum = sum_of_weighed_pixels(p, rows, cols, img, r)

        
