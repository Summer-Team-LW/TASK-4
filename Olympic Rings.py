#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2
import numpy as np

image= np.full((230,400 , 3),255, dtype = np.uint8)
cv2.circle(image,(70,95),50,[199,133,0],5)
cv2.circle(image,(190,95),50,[0,0,0],5)
cv2.circle(image,(310,95),50,[36,0,223],5)
cv2.circle(image,(130,160),50,[1,206,255],5)
cv2.circle(image,(250,160),50,[61,159,0],5)
         
cv2.imshow("Olympic Rings",image)
cv2.waitKey()
cv2.destroyAllWindows()

