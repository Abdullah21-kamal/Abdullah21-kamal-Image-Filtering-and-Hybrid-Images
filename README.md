# ** Hybrid Image Project ** 
**Overview**
This project demonstrates image filtering techniques to create hybrid images, which appear differently when viewed up close or at a distance. The project is based on the work by Oliva, Torralba, and Schyns (2006), focusing on blending high-frequency (sharp) and low-frequency (smooth) image content.

**Project Structure**
The repository includes the following components:

- Code: Functions to implement convolution and hybrid image creation.
- Documentation: Detailed explanations of image convolution, the differences between high-pass and low-pass filters, and the hybrid image concept.
- Testing: Scripts for testing the convolution function and visualizing hybrid images.
**Files and Directories**
- my_imfilter.py: Implements custom image convolution.
- hybrid_image.py: Combines high-pass and low-pass filtered images to create hybrid images.
- proj1_test_filtering.py: Testing script to validate convolution implementation.
- vis_hybrid_image.py: Visualization script for hybrid images.
images/: Contains example images and generated results.
README.md: Project overview and usage guide.
Getting Started

**Usage** 
* Image Filtering: Apply custom convolution with my_imfilter.py.
* Hybrid Image Creation: Combine two images with hybrid_image.py to create a hybrid image.
* Testing and Visualization: Use proj1_test_filtering.py and vis_hybrid_image.py to validate and view results.

**Features and Methods**
Image Convolution: Implemented from scratch to support arbitrary odd-dimension filters.
Hybrid Images: Blends two images with high- and low-frequency filtering for hybrid visualization.
**Requirements:**
The convolution algorithm should:
 Support grayscale and color images
- Handle odd-shaped filters (e.g., 3x3, 5x5)
- Generate output with identical resolution as the input
**Technical Details:**
- High-Pass and Low-Pass Filters: Used to isolate high- or low-frequency components in an image.
- Hybrid Image Creation: Combines a high-pass filter on one image and a low-pass filter on another to create a blended effect that changes with viewing distance.
**Extra Credit**
Implemented features:
- FFT-based convolution
- Reflection padding
- Additional hybrid image examples
**Acknowledgments**
This project is based on the course assignment by James Hays and Derek Hoiem. The hybrid image concept and examples are inspired by SIGGRAPH 2006 research by Oliva, Torralba, and Schyns.

