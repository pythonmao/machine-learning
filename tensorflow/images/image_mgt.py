from PIL import Image
from PIL import ImageOps

__author__ = 'maohaijun'
__COPYRIGHT__ = """(c) Copyright lenovo Corp. 2015, 2016. All rights reserved.
US Government Users Restricted Rights - Use, duplication or
disclosure restricted by GSA ADP Schedule Contract with lenovo Corp."""

# transpose
FLIP_LEFT_RIGHT = 0
FLIP_TOP_BOTTOM = 1
ROTATE_90 = 2
ROTATE_180 = 3
ROTATE_270 = 4

# resampling filters
NONE = 0
NEAREST = 0
ANTIALIAS = 1  # 3-lobed lanczos
LINEAR = BILINEAR = 2
CUBIC = BICUBIC = 3


def colorize(image, dir, black, white):
    """
    Colorize grayscale image.  The **black** and **white**
    arguments should be RGB tuples; this function calculates a color
    wedge mapping all black pixels in the source image to the first
    color, and all white pixels to the second color.

    :param image: The image to colorize.
    :param dir: output directory
    :param black: The color to use for black input pixels.
    :param white: The color to use for white input pixels.
    :return: An image.
    """

    try:
        im = Image.open(image)
        im = ImageOps.colorize(im, black=black, white=white)
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def grayscale(image, dir):
    '''
    Convert the image to grayscale.

    :param image: image name
    :param dir: output directory
    '''

    try:
        im = Image.open(image).convert("L")
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def rotate(image, dir, angle, resample=NEAREST, expand=0):
    '''
    :param image: image name
    :param dir: output directory
    :param angle: In degrees counter clockwise.
    :param resample: An optional resampling filter.  This can be
           one of :py:attr:`PIL.Image.NEAREST` (use nearest neighbour),
           :py:attr:`PIL.Image.BILINEAR` (linear interpolation in a 2x2
           environment), or :py:attr:`PIL.Image.BICUBIC`
           (cubic spline interpolation in a 4x4 environment).
           If omitted, or if the image has mode "1" or "P", it is
           set :py:attr:`PIL.Image.NEAREST`.
    :param expand: Optional expansion flag.  If true, expands the output
           image to make it large enough to hold the entire rotated image.
           If false or omitted, make the output image the same size as the
           input image.
    '''

    try:
        im = Image.open(image).rotate(angle, resample=resample, expand=expand)
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def shift(image, dir, width, height, fill=0):
    '''
    :param image: image name
    :param dir: output directory
    :param fill: Pixel fill value (a color value).  Default is 0 (black).
    '''

    try:
        im = Image.open(image)
        w, h = im.size
        im = ImageOps.expand(im,
                             border=(width, height, width + w,
                                     height + h), fill=fill)
        im = im.crop(box=(0, 0, w, h))
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def zoom(image, dir, width, height, resample=NEAREST):
    '''
    :param image: image name
    :param dir: output directory
    :param resample: An optional resampling filter.  This can be
           one of :py:attr:`PIL.Image.NEAREST` (use nearest neighbour),
           :py:attr:`PIL.Image.BILINEAR` (linear interpolation in a 2x2
           environment), :py:attr:`PIL.Image.BICUBIC` (cubic spline
           interpolation in a 4x4 environment), or
           :py:attr:`PIL.Image.ANTIALIAS` (a high-quality downsampling filter).
           If omitted, or if the image has mode "1" or "P", it is
           set :py:attr:`PIL.Image.NEAREST`.
    '''

    try:
        im = Image.open(image)
        im = im.resize((width, height), resample=resample)
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def mirror(image, dir, method=FLIP_LEFT_RIGHT):
    '''
    :param image: image name
    :param dir: output directory
    :param method: One of :py:attr:`PIL.Image.FLIP_LEFT_RIGHT`,
          :py:attr:`PIL.Image.FLIP_TOP_BOTTOM`, :py:attr:`PIL.Image.ROTATE_90`,
          :py:attr:`PIL.Image.ROTATE_180`, or :py:attr:`PIL.Image.ROTATE_270`.
    '''

    try:
        im = Image.open(image).transpose(method)
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def squash(image, dir, width, height, resample=NEAREST):
    '''
    :param image: image name
    :param dir: output directory
    :param resample: Optional resampling filter.  This can be one
           of :py:attr:`PIL.Image.NEAREST`, :py:attr:`PIL.Image.BILINEAR`,
           :py:attr:`PIL.Image.BICUBIC`, or :py:attr:`PIL.Image.ANTIALIAS`
           (best quality).  If omitted, it defaults to
           :py:attr:`PIL.Image.NEAREST` (this will be changed to ANTIALIAS in a
           future version).
    '''

    zoom(image, dir, width, height, resample=resample)


def crop(image, dir, width, height):
    '''
    :param image: image name
    :param dir: output directory
    '''

    try:
        im = Image.open(image).crop((0, 0, width, height))
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def fill(image, dir, width, height, fill=0):
    '''
    :param image: image name
    :param dir: output directory
    :param border:  Border width, in pixels.
    :param fill: Pixel fill value (a color value).  Default is 0 (black).
    '''

    try:
        im = Image.open(image)
        w, h = im.size
        im = ImageOps.expand(im, border=((width - w) / 2, (height - h) / 2,
                                         (width - w) / 2, (height - h) / 2), fill=fill)
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise


def half_fill_half_crop(image, dir, width, height, resample=NEAREST):
    '''
    Do resize to expand the image, then crop it.

    :param image: image name
    :param dir: output directory
    '''

    try:
        im = Image.open(image)
        w, h = im.size
        im = im.resize(((w + width) / 2, (h + height) / 2), resample=resample)
        im = im.crop(box=(0, 0, width, height))
        im.save(dir + '/' + image)
    except IOError:
        raise
    except Exception as exc:
        raise
