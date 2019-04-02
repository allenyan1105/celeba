import sys, os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import re

im = np.array(Image.open('/home/ubnt/datasets/celeba/train0-10000/images/005634.jpg'), dtype=np.uint8)

with open('/home/ubnt/datasets/celeba/train0-10000/labels/005634.txt') as f:
    lines = [line.rstrip('\n') for line in f]
#print lines
tokens =  lines[0].split(' ')
print tokens
x_min = int(tokens[4])
y_min = int(tokens[5])
w = int(tokens[6]) - int(tokens[4])
h = int(tokens[7]) - int(tokens[5])

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)

# Create a Rectangle patch
print x_min
print y_min
print w
print h
rect = patches.Rectangle((x_min,y_min),w,h,linewidth=1,edgecolor='w',facecolor='none')
#rect1 = patches.Rectangle((174.75, 25.6206),190.25,268.896,linewidth=1,edgecolor='r',facecolor='none')
# Add the patch to the Axes
ax.add_patch(rect)

#ax.add_patch(rect1)

plt.show()
