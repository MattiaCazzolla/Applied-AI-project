# Folder structure

    .
    ├── dataset_splitting                  # functions used for the resize and splitting in sets
    │   ├── split_and_resize.py          
    │   └── plot_folders.py  
    |
    ├── models                             # all models' notebooks and zip of final model
    │   ├── Densenet121
    |   ├── Efficientnetb2
    |   ├── Efficientnetb3
    |   ├── SVM
    |   ├── Scratch
    |   ├── VGG16
    |   └── model.zip
    |
    ├── preprocessing                      # binary classifiers and preprocessing function
    │   ├── binary_class_negative.ipynb
    |   ├── binary_class_random.ipynb
    |   └── preprocessing.py
    |
    ├── xai                                # notebooks for the different xai techniques
    │   ├── fairness-and-tsne.ipynb
    |   ├── Grad-CAM.ipynb
    |   ├── LIME.ipynb
    |   └── occlusion.py
    |
    └── dataset_exploration.ipynb          # notebook with data exploration results
