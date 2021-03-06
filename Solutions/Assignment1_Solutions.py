import cv2
import numpy as np

def binary_threshold(image, min_threshold, max_threshold):
    '''
        inputs:
            image: the source image, gray scale
            min_threshold: the minimum threshold of image
            max_threshold: the maximum threshold of image
        outputs:
            result: the output binary image
    '''
    result = image.copy()
    result[image<min_threshold] = 0
    result[image>min_threshold] = max_threshold
    
    return result

def binary_inv_threshold(image, min_threshold, max_threshold):
    '''
        inputs:
            image: the source image, gray scale
            min_threshold: the minimum threshold of image
            max_threshold: the maximum threshold of image
        outputs:
            result: the output binary inv image
    '''
    result = image.copy()
    result[image<min_threshold] = max_threshold
    result[image>min_threshold] = 0

    return result

def tozero_threshold(image, min_threshold):
    '''
        inputs:
            image: the source image, gray scale
            min_threshold: the minimum threshold of image
        outputs:
            result: the to zero image
    '''
    result = image.copy()
    result[image<=min_threshold] = 0

    return result

def zero_channel(image, channel):
    '''
        inputs:
            image: the source image, colord
            channel: the channel you want to make zero
        outputs:
            result: output image with zeroed channel
    '''

    result = image.copy()
    result[:, :, channel] = 0

    return result

def convert_to_gray(image):
    '''
        inputs:
            image: the source image, colord
        outputs:
            result: image in gray scale
    '''
    result = (np.sum(image, axis=2)/3).astype(np.uint8)

    return result

def divide_image_horizontally(image, divisions):
    '''
        inputs:
            image: the source image
            divisions: how many divisions you want in image horizontally
        output:
            result: a list of length=divisions, contains divided images
    '''    
    result = np.split(image, divisions, axis=1)
        
    return result

def divide_image_vertically(image, divisions):
    '''
        inputs:
            image: the source image
            divisions: how many divisions you want in image vertically
        output:
            result: a list of length=divisions, contains divided images
    '''    
    result = np.split(image, divisions, axis=0)
    
    return result