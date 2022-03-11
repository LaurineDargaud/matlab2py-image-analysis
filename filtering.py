"""
MATLAB2Py - Image Analysis: Filtering
"""

__version__ = "0.1.0"

def fspecial(type: str, hsize = 3, sigma = None):
    """
    Return a predefined 2D filter
    :param type: type of filter ('gaussian','prewitt','sobel')
    :type type: str
    :param hsize: size of filter, default to 3
    :type hsize: int(, optional)
    :param sigma: standard deviation for Gaussian filter, default to 1.
    :type sigma: float(, optional)
    :return: a 2D filter
    :rtype: array
    """