import cv2
import os
import numpy as np

files = os.listdir(os.getcwd() + '/frames/')

lap =0
count = 0
for f in files:
    img = cv2.imread(os.getcwd() + '/frames/' + f,cv2.IMREAD_GRAYSCALE)
    fm = cv2.Laplacian(img,cv2.CV_64F).var()
    lap = fm + lap
    count = count + 1
    
print('Average varaince for Undistored')        
print(lap/count)
