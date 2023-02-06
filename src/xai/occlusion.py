import os
import cv2
import numpy as np
import matplotlib.pyplot as plt


def occlusion(img, block_size):
    '''
    Given an image it generate all the possible occlusions
    with a block of black pixels
    '''
    
    h, w = img.shape
    columns = h // block_size
    rows =  w // block_size
    
    array = np.concatenate([np.expand_dims(img, axis=0) for i in range (rows*columns)], axis=0)
    
    k=0
    for row in range(rows):
        for column in range(columns):
            
            x = column*block_size
            y = row*block_size
            
            top = int(y)
            left = int(x)
            right = left+block_size
            bottom = top+block_size
            
            array[k, int(top):int(bottom), int(left):int(right)] = np.zeros((block_size, block_size))
            k+=1

    return array


def occlusion_heatmap(img, label_idx, block_size, model):
    '''
    Given an image, it generates the occlusions and produce an 
    heatmap related to the variation of predicion
    '''

    occluded_images = occlusion(img, block_size)
    occluded_images = np.expand_dims(occluded_images, axis=-1)
    
    predictions = model.predict(occluded_images)
    predictions = predictions[:,label_idx]
    
    predictions = np.reshape(predictions,(int(np.sqrt(len(predictions))), int(np.sqrt(len(predictions)))))
    
    heatmap = cv2.resize(predictions,(256,256)) 
    heatmap *= 255
    heatmap = np.uint8(heatmap)
    heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
    heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)
    
    return heatmap


def get_overlay(img, heatmap):
    '''
    Given an image and a heatmap it produce the overlay
    '''

    overlayed = cv2.addWeighted(img, 1, heatmap, 0.40, 0)
    return overlayed


def explain_occlusion(img, label, model, block_size):
    '''
    Given an image it visualize the results of the occlusion method
    '''

    heatmap = occlusion_heatmap(img, label, block_size, model)
    overlay = get_overlay(img, heatmap) 

    plt.figure(figsize=(10,7))
    
    plt.subplot(1,2,1)
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.title(f'label: {label}')
    
    plt.subplot(1,2,2)
    plt.imshow(overlay)
    plt.axis('off')
