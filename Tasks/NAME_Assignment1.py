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

    return result

def tozero_threshold(image, min_threshold):
    '''
        inputs:
            image: the source image, gray scale
            min_threshold: the minimum threshold of image
        outputs:
            result: the to zero image
    '''

    return result

def zero_channel(image, channel):
    '''
        inputs:
            image: the source image, colored
            channel: the channel you want to make zero
        outputs:
            result: output image with zeroed channel
    '''

    return result

def convert_to_gray(image):
    '''
        inputs:
            image: the source image, colored
        outputs:
            result: image in gray scale
    '''

    return result

def divide_image_horizontally(image, divisions):
    '''
        inputs:
            image: the source image, colored or gray scale
            divisions: how many divisions you want in image horizontally
        output:
            result: a list of length=divisions, contains divided images
    '''    

    return result

def divide_image_vertically(image, divisions):
    '''
        inputs:
            image: the source image, colored or gray scale
            divisions: how many divisions you want in image vertically
        output:
            result: a list of length=divisions, contains divided images
    '''    

    return result