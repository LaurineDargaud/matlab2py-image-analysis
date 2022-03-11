"""
MATLAB2Py - Image Analysis: Filtering
"""

__version__ = "0.1.0"

import matplotlib.pyplot as plt
import numpy as np
import cv2

def fspecial(type: str, hsize:int = 3, sigma:float = 1.):
    """
    Return a predefined 2D filter
    :param type: type of filter ('gaussian','prewitt','sobel')
    :type type: str
    :param hsize: size of filter, defaults to 3
    :type hsize: int, optional
    :param sigma: standard deviation for Gaussian filter, defaults to 1.0
    :type sigma: float, optional
    :return: a 2D filter
    """
    if type == 'sobel':
        return get_sobel(hsize)
    if type == 'prewitt':
        return get_prewitt(hsize)
    if type == 'gaussian':
        return get_gaussian(hsize, sigma)

def get_sobel(size):
    """ Return a Sobel filter of given size (x-sensitive)"""
    sobelX = cv2.getDerivKernels(1, 0, size)
    return - np.outer(sobelX[0], sobelX[1])

def get_prewitt(size):
    """ Return a Prewitt filter of given size (x-sensitive)"""
    value = (size - 1)//2
    rows_list = [np.zeros(size)]
    for i in range (value):
        coeff = i+1
        rows_list = [coeff * np.ones(size)] + rows_list
        rows_list.append(-coeff * np.ones(size))
    prewitt_flat = np.concatenate(rows_list)
    return np.reshape(prewitt_flat, (size, size))

def get_gaussian(size, sigma):
    """ Return a Gaussian kernel with given side length and sigma """
    size, sigma = int(size), float(sigma)
    ax = np.linspace(-(size - 1) / 2., (size - 1) / 2., size)
    gauss = np.exp(-0.5 * np.square(ax) / np.square(sigma))
    kernel = np.outer(gauss, gauss)
    return kernel / np.sum(kernel)

