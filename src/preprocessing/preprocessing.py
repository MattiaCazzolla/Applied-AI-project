import numpy as np
from skimage import filters
import cv2

def preprocessing(image):
    
    # Thresholding the image using Otsu:
    th = filters.threshold_otsu(image)
    bw_image = image > th
    
    roi_crop = bw_image[216:, (128-40):(128+40)]
    
    # Invert negative image:
    thr_neg = 0.99
    sum_roi_crop = np.sum(roi_crop)
    ratio_roi_crop = sum_roi_crop/(roi_crop.shape[0]*roi_crop.shape[1])
    
    # Median filtering:
    thr_med = 0.02
    arr = roi_crop.astype('float16')
    arr2 = np.append(arr[:,1:], np.expand_dims(arr[:,-1], axis = -1), axis = 1)   
    flips = np.sum(np.abs(arr-arr2), axis=(0,1)) / (arr.shape[0]*arr.shape[1])
    
    if((1 - ratio_roi_crop) >= thr_neg):
        new_image = 255 - image
    elif(flips >= thr_med):
        new_image = cv2.medianBlur(image.astype('float32'), ksize = 5)
    else:
        new_image = image
    
    # Histogram Equalization
    image_histogram, bins = np.histogram(new_image.flatten(), 256, density=True)
    cdf = image_histogram.cumsum() 
    cdf = (256-1) * cdf / cdf[-1] 

    # use linear interpolation of cdf to find new pixel values
    image_equalized = np.interp(new_image.flatten(), bins[:-1], cdf)
    image_equalized = image_equalized.reshape(new_image.shape)
        
    return image_equalized