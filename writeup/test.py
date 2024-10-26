import numpy as np
import scipy.ndimage as ndi
import skimage.io as io
import skimage.transform as tf
import time

def time_filter_size(image, filter_sizes, image_size):
    times = []
    for size in filter_sizes:
        # Create a square filter of the given size
        filter_ = np.ones((size, size)) / (size**2)

        # Resize the image to the given size
        image_resized = tf.resize(image, (image_size, image_size))

        # Measure the computation time for convolving the filter with the resized image
        start_time = time.time()
        ndi.convolve(image_resized, filter_)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


def time_image_size(image, image_sizes, filter_size):
    times = []
    for size in image_sizes:
        # Create a square filter of the given size
        filter_ = np.ones((filter_size, filter_size)) / (filter_size**2)

        # Resize the image to the given size
        image_resized = tf.resize(image, (size, size))

        # Measure the computation time for convolving the filter with the resized image
        start_time = time.time()
        ndi.convolve(image_resized, filter_)
        end_time = time.time()
        times.append(end_time - start_time)
    return times


# Load the input image
image = io.imread('RISDance.jpg', as_gray=True)

# Define the filter sizes and image sizes to test
filter_sizes = list(range(3, 16, 2))  # odd and square filter sizes from 3x3 to 15x15
image_sizes = [int(2**i) for i in np.arange(8, 21, 1)]  # image sizes from 0.25 MPix to 8 MPix

# Measure the computation times for various filter sizes and image sizes
filter_times = np.array([time_filter_size(image, filter_sizes, size) for size in image_sizes])
image_times = np.array([time_image_size(image, image_sizes, size) for size in filter_sizes])


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Plot the results as a surface plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(filter_sizes, image_sizes)
ax.plot_surface(X, Y, filter_times, cmap='viridis')
ax.set_xlabel('Filter size')
ax.set_ylabel
