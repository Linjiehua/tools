import cv2 as cv
from glob import glob
import os
import numpy as np
label_dir='/home/a123/js_dataset/labels/'
image_dir='/home/a123/js_dataset/images/'
save_dir='/home/a123/js_dataset/detection/'
images=sorted(glob(image_dir+'/*.tif'))
labels=sorted(glob(label_dir+'/*.txt'))
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
for _id,image in enumerate(images):
    label=labels[_id]
    image_n=image.split('/')[-1]
    save_name=os.path.join(save_dir,image_n)
    image_name=image.split('/')[-1].split('.')[0]
    label_name=label.split('/')[-1].split('.')[0]
    if not label_name==image_name:
        print('image name is not equal with label name ')
        continue
    im=cv.imread(image)
    with open(label,'r') as f:
        for _id_,line in enumerate(f.readlines()):
            line=line.split(' ')
            box=[[int(line[1]),int(line[2])],[int(line[3]),int(line[4])],
                 [int(line[5]),int(line[6])],[int(line[7]),int(line[8])]]
            box=np.array(box)
            #print(box)
            im=cv.drawContours(im,[box],-1, (255,0,255),1,1)
    cv.imwrite(save_name,im)