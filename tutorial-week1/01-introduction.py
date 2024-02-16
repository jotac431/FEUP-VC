#!/usr/bin/env python
# coding: utf-8

# # Lab 1: Introduction to OpenCV

# The goal of this first lab is to present a small introduction to image processing using OpenCV. In each section, you can find:
# * a small example - analyse the code and try it
# * some exercises

# In[ ]:


# Requirements for this tutorial
get_ipython().system(' pip install opencv-python')
get_ipython().system(' pip install numpy')


# In[ ]:


# If you prefer, you can convert this notebook to a Python script by uncommenting the following command
get_ipython().system(' pip install nbconvert')
get_ipython().system(' jupyter nbconvert --to script 01-introduction.ipynb')


# In[ ]:


import cv2
import numpy as np
import os

dataDir = './data'


# ### 1. Images – read, write and display; ROIs

# In[ ]:


# Opening an image
img = cv2.imread(os.path.join(dataDir, 'ml.jpg'))

# Showing the image
cv2.imshow("ml.jpg", img)

# Waiting for user to press a key to close the image
cv2.waitKey(0)

# Close the window after user pressed a key
cv2.destroyWindow("ml.jpg")


# In[ ]:


# Check image size
h, w, c = img.shape
print(f'height: {h}')
print(f'width: {w}')
print(f'channels: {c}')


# In[ ]:


# Saving image in bmp format
cv2.imwrite('ml_new.bmp', img)


# Exercise 1.1 - Read any other color image from a file, show the mouse cursor over the image, and the coordinates and RGB components of the pixel under the cursor. When the user clicks on the mouse, let him modify the RGB components of the selected pixel.

# In[ ]:


# TODO


# Exercise 1.2 - Allow the user to select a region of interest (ROI) in the image, by clicking on two points that identify two opposite corners of the selected ROI, and save the ROI into another file.

# In[ ]:


# TODO


# ### 2. Images – representation, grayscale and color, color spaces

# In[ ]:


# Create a white image
m = np.ones((100,200,1), np.uint8)

# Change the intensity to 100
m = m * 100

# Display the image
cv2.imshow('Grayscale image', m)
cv2.waitKey(0)
cv2.destroyWindow('Grayscale image')


# In[ ]:


# Draw a line with thickness of 5 px
cv2.line(m, (0,0), (200,100), 255, 5)
cv2.line(m, (200, 0), (0, 100), 255, 5)
cv2.imshow('Grayscale image with diagonals', m)
cv2.waitKey(0)
cv2.destroyWindow('Grayscale image with diagonals')


# Exercise 2.1 - Create a color image with 100(lines)x200(columns) pixels with yellow color; draw the two diagonals of the image, one in red color, the other in blue color. Display the image.

# In[ ]:


# TODO


# Exercise 2.2 - Read any color image, in RGB format, display it in one window, convert it to grayscale, display the grayscale image in another window and save the grayscale image to a different file

# In[ ]:


# TODO


# Exercise 2.3 - Split the 3 RGB channels and show each channel in a separate window. Add a constant value to one of the channels, merge the channels into a new color image and show the resulting image.

# In[ ]:


# TODO


# Exercise 2.4 - Convert the image to HSV, split the 3 HSV channels and show each channel in a separate window. Add a constant value to saturation channel, merge the channels into a new color image and show the resulting image.

# In[ ]:


# TODO


# ### 3. Video – acquisition and simple processing

# In[ ]:


# Define a VideoCapture Object
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

frame_nr = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # If frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Display the resulting frame
    cv2.imshow('webcam', frame)

    # Wait for user to press s to save frame
    if cv2.waitKey(1) == ord('s'):
        frame_name = 'frame' + str(frame_nr) + '.png'
        cv2.imwrite(frame_name, frame)
        cv2.imshow("Saved frame: " + frame_name, frame)
        cv2.waitKey(0)
        cv2.destroyWindow("Saved frame: " + frame_name)

    # Wait for user to press q to quit
    if cv2.waitKey(1) == ord('q'):
        break

    frame_nr += 1

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()


# Exercise 3.1 - Using the previous example as the baseline, implement a script that acquires the video from the webcam, converts it to grayscale, and shows the frames in binary format (i.e. the intensity of each pixel is 0 or 255); use a threshold value of 128.

# In[ ]:


# TODO


# Exercise 3.2 - Implement a simple detection/tracking algorithm for colored objects, using the following steps:
# 1) take each frame of the video;
# 2) convert from BGR to HSV color-space;
# 3) threshold the HSV image for a range of color values (creating a binary image);
# 4) extract the objects of the selected range (with a bitwise AND operation, using as operands the original and the binary image).

# In[ ]:


# TODO

