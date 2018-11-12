import cv2
import numpy as np
import os

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)
   
   
   
files = os.listdir(os.getcwd() + '/dark/')

count = 0

for f in files:
    original = cv2.imread(os.getcwd() + '/dark/' + f,1)
    #cv2.imshow('original',original)
    
    label = f.split('.')[0][5:]
    #print(label)
    
    gamma = 4.5                # change the value here to get different result
    adjusted = adjust_gamma(original, gamma=gamma)
    #cv2.putText(adjusted, "g={}".format(gamma), (10, 30),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    #cv2.imshow("gammam image 1", adjusted)
    #cv2.imwrite('new_image.png',adjusted)
    gray_image = cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray_image)
    
    #cv2.imshow("Equalization",equ)
    
    
    
    color_yuv = cv2.cvtColor(original,cv2.COLOR_BGR2YUV)
    
    color_yuv[:,:,0] = cv2.equalizeHist(color_yuv[:,:,0])
    
    img_output = cv2.cvtColor(color_yuv, cv2.COLOR_YUV2BGR)
    
    
    
    #cv2.imshow("Colored Equalization",img_output)
    cv2.imwrite("C:/ML/tlevels/dark_corrc/frame%d.jpg" % int(label), equ)
    
    count +=1
