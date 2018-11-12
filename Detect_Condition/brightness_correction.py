import cv2
import numpy as np
import os


files = os.listdir(os.getcwd() + '/bright/')

count = 0

for f in files:
    img = cv2.imread(os.getcwd() + '/bright/' + f,1)
    #cv2.imshow('original',original)
    
    label = f.split('.')[0][5:]

    alpha = 0.8

    beta = -60

    result = cv2.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)

    
    cv2.imwrite("C:/ML/tlevels/bright_corrc/wo_equi/frame%d.jpg" % int(label), result)

    gray_image = cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)

    # create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(gray_image)

    cv2.imwrite("C:/ML/tlevels/bright_corrc/w_equi/frame%d.jpg" % int(label), cl1)
    
    count += 1
