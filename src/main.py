import numpy as np
from skimage import data

i = data.astronaut()

import matplotlib.pyplot as plt

plt.grid(False)
plt.gray()
plt.axis('off')
plt.imshow(i)
plt.show()      # shows the image of an astronaut

i_transformed = np.copy(i)
size_x = i_transformed.shape[0]
size_y = i_transformed.shape[1]

filter1 = [ [-1, -2, -1], [0, 0, 0], [1, 2, 1]]
filter2 = [ [0, 1, 0], [1, -4, 1], [0, 1, 0]]
filter3 = [ [-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] # all values sum to 0

weight = 1 

i_transformed = np.zeros_like(i)
filter = np.array(filter1)

for x in range(1, size_x - 1):
    for y in range(1, size_y - 1):
        convolution = 0.0

        for fx in range(3):
            for fy in range(3):
                convolution += i[x + fx - 1, y + fy - 1] * filter[fx, fy]
        convolution *= weight
        convolution = np.clip(convolution, 0, 255)
        i_transformed[x, y] = convolution

plt.gray()
plt.grid(False)
plt.imshow(i_transformed)
plt.axis('off')
plt.show()  # shows the transformed image after applying the filter

# If we want to extract more vertical or horizontal lines, 
# It depends on the filter we use. 

# What is MAX pooling? Why do we use it?
# MAX pooling is a down-sampling technique used in convolutional neural networks (CNNs).
# It reduces the spatial dimensions of the input feature map by taking the maximum value in each pooling window.
# This helps to retain the most important features while reducing the computational load and preventing overfitting.
# MAX pooling is typically used after convolutional layers to reduce the size of the feature maps.

new_x = int(size_x / 2)
new_y = int(size_y / 2)
new_image = np.zeros((new_x, new_y))

for x in range(0, size_x - 1, 2):
    for y in range(0, size_y - 1, 2):
        
        pixels = [
            i_transformed[x, y], i_transformed[x + 1, y],
            i_transformed[x, y + 1], i_transformed[x + 1, y + 1]
        ]

        if isinstance(pixels[0], np.ndarray):
            pixels = [max(p.max() for p in pixel) if isinstance(pixel, np.ndarray) else float(pixel) for pixel in pixels]
        pixels.sort(reverse=True)
        new_image[int(x / 2), int(y / 2)] = pixels[0]

plt.gray()
plt.grid(False)
plt.imshow(new_image)
plt.axis('off')
plt.show()  # shows the image after applying MAX pooling

