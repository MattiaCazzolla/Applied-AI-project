# Chest-X-Rays-Image-Classification
Chest X-Rays Image Classification project made by me ([@stevanna98](https://github.com/stevanna98)) and my collegues for the course Applied AI in Biomedicine at Politecnico di Milano
- ####  Mattia Cazzolla  ([@MattiaCazzolla](https://github.com/MattiaCazzolla)) mattia.cazzolla@mail.polimi.it
- ####  Sara Ghezzi () sara1.ghezzi@mail.polimi.it
- ####  Stefano Vannoni ([@stevanna98](https://github.com/stevanna98)) stefano.vannoni@mail.polimi.it

## Data
The provided dataset contais 15470 labeled images of healthy individuals and individuals affected by either Pneumonia or Tuberculosis.

<p align="center">
<img src="/imgs/classes.jpeg" alt="">
</p>

The dataset is unbalanced with the normal, pneumonia and tuberculosis classes representing respectively the 60%, 27% and 13% of the data

## Models

We trained and tested a multitude of models, comparing them with the F1 score metric on the validation set

| Model | F1 - Normal | F1 - Pneumonia | F1 - Tuberculosis | 
|:-----------|:----------------------:|:--:|:--:|
| SVM (HOGs) | 0.927 | 0.953 | 0.771 |
| CNN Scratch | 0.969 | 0.980 | 0.882 |
| EfficientNetB2 | **0.982** | 0.981 | **0.936** |
| EfficientNetB3 | 0.978 | 0.982 | 0.921 |
| DenseNet121 | 0.968 | 0.976 | 0.883 |
| VGG16 | 0.974 | **0.983** | 0.900 |

## Evaluation

We chose *EfficientNetB2* as our best model and we evaluated it on the test set

| Model | F1 - Normal | F1 - Pneumonia | F1 - Tuberculosis | 
|:-----------|:----------------------:|:--:|:--:|
| EfficientNetB2 | 0.975 | 0.977 | 0.921 |

<br>
<img src="/imgs/cm.png" alt="">

