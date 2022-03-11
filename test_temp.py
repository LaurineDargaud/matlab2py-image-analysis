def fspecial2(type: str, hsize: int = 3, sigma: float = 1.):
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