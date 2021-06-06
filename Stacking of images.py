#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy

image1=cv2.imread("Design1.png")
image2=cv2.imread("Design2.png")

pic=numpy.hstack((image1,image2))
pic1=numpy.vstack((image1,image2))

cv2.imshow("Horizontal stacking",pic)
cv2.waitKey()
cv2.destroyAllWindows()

