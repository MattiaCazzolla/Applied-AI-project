import os
import pandas as pd
import cv2

def split_classes(src, dst, csv_file_path):
    '''
    Given a src folder with all the images and a csv file with the 
    label for each image, it divide the image in subfolders specific
    for each class
    '''

    df = pd.read_csv(csv_file_path)
    files = df['file'].tolist()
    labels = df['label'].tolist()

    for file,label in zip(files,labels):
        old_path = os.path.join(src,file)
        new_path = os.path.join(dst,label)
        new_path = os.path.join(new_path, file)
        os.rename(old_path, new_path)

def resize(src):
    '''
    Given a folder with the images divided in subfolders based on classes
    it reseize each image to 256x256
    '''
    labels = os.listdir(src)
    for label in labels:
        dir_label = os.path.join(src, label)
        files = os.listdir(dir_label)
        for file in files:
            file_path = os.path.join(dir_label,file)
            img = cv2.imread(file_path)
            resize_img = cv2.resize(img, (256,256))
            cv2.imwrite(file_path, resize_img)


