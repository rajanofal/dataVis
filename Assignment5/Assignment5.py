import numpy as np
from matplotlib import pyplot as plt
from scipy.ndimage import rotate
import copy

data = np.fromfile('volume.raw', dtype='uint16', sep="")


image = np.reshape(data, (421, 512, 512))


image1 = image[0,:,:]
image2 = image[420,:,:]

plt.figure()
plt.imshow(image1, cmap='gray')
plt.title('Original Image 1')
plt.show()

plt.figure()
plt.imshow(image2, cmap='gray')
plt.title('Original Image 2')
plt.show()

# Task A
temp1 = copy.deepcopy(image)
taska = np.sum(temp1, axis=1)

plt.figure()
plt.imshow(taska, cmap='gray')
plt.title('View from Y Axis')
plt.show()

# Task B
temp2 = copy.deepcopy(image)

# Took help for the rotate function from stackoverflow
rot = rotate(temp2, angle=-45, reshape=False) # rotating the data -45 degrees

taskb = np.sum(rot, axis=1)

plt.figure()
plt.imshow(taskb, cmap='gray')
plt.title('View from 45 degree Angle')
plt.show()