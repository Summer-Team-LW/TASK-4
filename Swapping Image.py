#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cv2
import numpy

image1=cv2.imread("Design1.png")
image11=cv2.imread("Design1.png")
image2=cv2.imread("Design2.png")

tmp=image1[70:400,70:200]
image1[70:400,70:200]=image2[70:400,70:200]
image2[70:400,70:200]=image11[70:400,70:200]

cv2.imshow("Swapped image1",image1)
cv2.waitKey()
cv2.destroyAllWindows()

