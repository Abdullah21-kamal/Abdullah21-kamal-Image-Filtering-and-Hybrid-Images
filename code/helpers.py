# Project Image Filtering and Hybrid Images Stencil Code
# Based on previous and current work
# by James Hays for CSCI 1430 @ Brown and
# CS 4495/6476 @ Georgia Tech
import numpy as np
from numpy import pi, exp, sqrt
from skimage import io, img_as_ubyte, img_as_float32
from skimage.transform import rescale
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean



def my_imfilter(image: np.ndarray, filter: np.ndarray):
  """
  Your function should meet the requirements laid out on the project webpage.
  Apply a filter to an image. Return the filtered image.
  Inputs:
  - image -> numpy nd-array of dim (m, n, c) for RGB images or numpy nd-array of dim (m, n) for gray scale images
  - filter -> numpy nd-array of odd dim (k, l)
  Returns
  - filtered_image -> numpy nd-array of dim (m, n, c) or numpy nd-array of dim (m, n)
  Errors if:
  - filter has any even dimension -> raise an Exception with a suitable error message.
  """
  #filtered_image = np.asarray([0])
  # Your code here #

  [i, j] = filter.shape
  r = image.shape[0]
  c = image.shape[1]
  number_of_channels = image.shape[2]

  conv_result=np.zeros((r+i-1,c+j-1,number_of_channels))
  for x in range(number_of_channels):
    image_padding = np.pad(image[:,:,x], (i//2, j//2), 'constant', constant_values=(0, 0))

    for y in range(c+j-1):
        for z in range(r+i-1):
            for k in range(j):
                for l in range(i):
                  if y-k>0 and z-l>0:
                    conv_result[z,y,x] = conv_result[z,y,x] + filter[l,k]*image_padding[z-l,y-k]

  filtered_image = conv_result[0: (r),0: (c),:]

  return filtered_image

def create_gaussian_filter(side_length, sigma):
    # create an empty numpy array with the specified side length
    kernel = np.empty((side_length, side_length))

    # calculate the center of the kernel
    center = (side_length - 1) / 2.

    # calculate the scaling factor
    factor = -0.5 / (sigma * sigma)

    # calculate the values of the kernel
    for i in range(side_length):
        for j in range(side_length):
            x = i - center
            y = j - center
            kernel[i, j] = np.exp(factor * (x * x + y * y))

    # normalize the kernel
    kernel /= np.sum(kernel)

    return kernel

def gen_hybrid_image(image1: np.ndarray, image2: np.ndarray, cutoff_frequency: float):
  """
   Inputs:
   - image1 -> The image from which to take the low frequencies.
   - image2 -> The image from which to take the high frequencies.
   - cutoff_frequency -> The standard deviation, in pixels, of the Gaussian
                         blur that will remove high frequencies.

   Task:
   - Use my_imfilter to create 'low_frequencies' and 'high_frequencies'.
   - Combine them to create 'hybrid_image'.
  """

  assert image1.shape == image2.shape

  # Steps:
  # (1) Remove the high frequencies from image1 by blurring it. The amount of
  #     blur that works best will vary with different image pairs
  # generate a gaussian kernel with mean=0 and sigma = cutoff_frequency,
  # Just a heads up but think how you can generate 2D gaussian kernel from 1D gaussian kernel
  side_length = 7
  kernel = create_gaussian_filter(side_length, cutoff_frequency)

  # Your code here:
  low_frequencies = my_imfilter(image1, kernel) # Replace with your implementation

  # (2) Remove the low frequencies from image2. The easiest way to do this is to
  #     subtract a blurred version of image2 from the original version of image2.
  #     This will give you an image centered at zero with negative values.
  # Your code here #
  high_frequencies = image2-my_imfilter(image2, kernel)  # Replace with your implementation

  # (3) Combine the high frequencies and low frequencies
  # Your code here #
  hybrid_image = low_frequencies+high_frequencies # Replace with your implementation

  # (4) At this point, you need to be aware that values larger than 1.0
  # or less than 0.0 may cause issues in the functions in Python for saving
  # images to disk. These are called in proj1_part2 after the call to
  # gen_hybrid_image().
  # One option is to clip (also called clamp) all values below 0.0 to 0.0,
  # and all values larger than 1.0 to 1.0.
  hybrid_image=np.clip(hybrid_image,0,1)


  # (5) As a good software development practice you may add some checks (assertions) for the shapes
  # and ranges of your results. This can be performed as test for the code during development or even
  # at production!

  return low_frequencies, high_frequencies, hybrid_image

def vis_hybrid_image(hybrid_image: np.ndarray):
  """
  Visualize a hybrid image by progressively downsampling the image and
  concatenating all of the images together.
  """
  scales = 5
  scale_factor = 0.5
  padding = 5
  original_height = hybrid_image.shape[0]
  num_colors = 1 if hybrid_image.ndim == 2 else 3

  output = np.copy(hybrid_image)
  cur_image = np.copy(hybrid_image)
  for scale in range(2, scales+1):
    # add padding
    output = np.hstack((output, np.ones((original_height, padding, num_colors),
                                        dtype=np.float32)))
    # downsample image
    cur_image = rescale(cur_image, scale_factor, mode='reflect', channel_axis=2)
    # pad the top to append to the output
    pad = np.ones((original_height-cur_image.shape[0], cur_image.shape[1],
                   num_colors), dtype=np.float32)
    tmp = np.vstack((pad, cur_image))
    output = np.hstack((output, tmp))
  return output

def load_image(path):
  return img_as_float32(io.imread(path))

def save_image(path, im):
  return io.imsave(path, img_as_ubyte(im.copy()))
