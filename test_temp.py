def square(a):
    """short description of the function square

    longish explanation: returns the square of a: :math:`a^2`

    :param a: an input argument

    :returns: a*a
    """
    return a*a

def fspecial(type: str, hsize: int = 3, sigma: float = 1.):
    """Return a predefined 2D filter

    :param type: type of filter ('gaussian','prewitt','sobel')
    :type type: str
    :param hsize: size of filter, defaults to 3
    :type hsize: int, optional
    :param sigma: standard deviation for Gaussian filter, defaults to 1.0
    :type sigma: float, optional

    :returns: a 2D filter
    """
    if type == 'sobel':
        return get_sobel(hsize)
    if type == 'prewitt':
        return get_prewitt(hsize)
    if type == 'gaussian':
        return get_gaussian(hsize, sigma)