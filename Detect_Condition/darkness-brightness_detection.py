from PIL import Image
import os

files = os.listdir(os.getcwd() + '/bright/')

new_brightness = 0
count = 0

for f in files:
    path = os.getcwd() + '/bright/' + f
    #img = cv2.imread(os.getcwd() + '/frames/' + f,cv2.IMREAD_GRAYSCALE)
    imag = Image.open(path)
    #Convert the image te RGB if it is a .gif for example
    imag = imag.convert ('RGB')
    #coordinates of the pixel
    X,Y = 0,0
    #Get RGB
    pixelRGB = imag.getpixel((X,Y))
    R,G,B = pixelRGB 

    brightness = sum([R,G,B])/3 ##0 is dark (black) and 255 is bright (white)
    
    new_brightness += brightness

    count = count + 1

print(new_brightness/count)
