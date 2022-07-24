
import cv2
import glob
import os
import random
import datetime


# Get images
imgs = glob.glob('*.jpg')
imgs.extend(glob.glob('*.png'))

print('Found files:')
print(imgs)

width = 2000 # CHANGE THIS NUMBER 
print('Resizing all images be %d pixels wide' % width)

folder = 'resized'
if not os.path.exists(folder):
    os.makedirs(folder)

# Iterate through resizing and saving
for img in imgs:
    timestamp='{:%Y-%m-%d-%H%M%S}'.format(datetime.datetime.now())
    randthingy=str(random.randint(1000,9999))
    print(randthingy)
    pic = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    height = int(width * pic.shape[0] / pic.shape[1])
    pic = cv2.resize(pic, (width, height))
    newimg = timestamp+randthingy+".jpg"
    print(newimg)
    cv2.imwrite(folder + '/' + newimg, pic)
