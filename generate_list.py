from glob import glob

image_dir='/home/a123/js_dataset/val/images/'

images=sorted(glob(image_dir+'/*.tif'))

print(images)
with open('/home/a123/js_dataset/val/test.txt','w') as f:
    for _id,image in enumerate(images):
        im_name=image.split('/')[-1].split('.')[0]
        print(im_name)
        f.writelines(im_name+'\n')