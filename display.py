def imshow(I, grayscale_filter = None, title = None, figsize = None, cmap = 'gray', display_grid = False, gridcolor = 'w', gridwidth = 2, linestyle='-'):
    """Display image

    :param I: image
    :param grayscale_filter: grayscale image display range as [low, high]
    :param title: title of the figure
    :param cmap: cmap of display
    :param display_grid: set to `True` to draw a pixel grid on top of the image

    :returns: None
    """
    anImage = deepcopy(I)
    if figsize != None:
        plt.figure(figsize=figsize)
    if grayscale_filter != None:
        min_scale, max_scale = grayscale_filter
        anImage[(anImage<min_scale) | (anImage>max_scale)] = 0
    plt.imshow(anImage, cmap=cmap)
    if title != None:
        plt.title(title)
    if display_grid:
        _display_grid(anImage, gridcolor, gridwidth, linestyle)
    else:
        plt.axis('off')
    plt.show()

def plot_images(images, figsize=(10,5), cmap='gray', display_grid = False, gridcolor='w', gridwidth=2, linestyle='-'):
    """Plot several images (max 10)

    :param images: a list of images as [[<image>, <title>]]
    :param figsize: the size of final figure
    :param cmap: cmap of display
    :param display_grid: set to `True` to draw a pixel grid on top of the image

    :returns: None
    """
    plt.figure(figsize=figsize)
    for i in range (len(images)):
        anImage, aTitle = images[i]
        plt.subplot(100+len(images)*10+i+1)
        plt.imshow(anImage, cmap=cmap)
        plt.title(aTitle)
        if display_grid:
            _display_grid(anImage, gridcolor, gridwidth, linestyle)
        else:
            plt.axis('off')
    plt.show()

def _display_grid(anImage, gridcolor, gridwidth, linestyle):
    """ Display grid on picture """
    X,Y = anImage.shape
    ax = plt.gca();
    # Major ticks
    ax.set_xticks(np.arange(0, X, 1))
    ax.set_yticks(np.arange(0, Y, 1))
    # Labels for major ticks
    ax.set_xticklabels(np.arange(1, X+1, 1))
    ax.set_yticklabels(np.arange(1, Y+1, 1))
    # Minor ticks
    ax.set_xticks(np.arange(-.5, X, 1), minor=True)
    ax.set_yticks(np.arange(-.5, Y, 1), minor=True)
    # Gridlines based on minor ticks
    ax.grid(which='minor', color=gridcolor, linestyle=linestyle, linewidth=gridwidth)