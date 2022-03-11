import header

def imhist(I, n:int = 20, figsize = (15,5), filename:str = 'Image'):
    """Return and display the histogram of image data

    :param I: grayscale image
    :param n: number of bins, defaults to 20
    :type n: int
    :param figsize: figsize of figure
    :param filename: name of given image, to insert in title
    :type filename: str

    :returns: [histogram counts, bin locations]
    """
    plt.figure(figsize=figsize)
    counts, binLocations, _ = plt.hist(I.flatten(), bins=list(range(256)))
    plt.title(f'Histogram of {filename}')
    plt.xticks(np.linspace(0,256,n).astype(int))
    plt.show()
    return [counts, binLocations]