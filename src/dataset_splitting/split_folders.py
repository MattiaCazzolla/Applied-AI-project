import os
import random
import multiprocessing
import shutil

def split_folders(src, dst, ratio=(0.8,0.1,0.1), seed=None):
    '''
    Given a src folder with the images divided in the N, P, T subfolders
    create the train, val, test split with images from same patient in same set
    '''
    
    if sum(ratio) != 1:
        raise Exception("Sum of ratio should be 1")
    
    if not os.path.exists(dst):
        os.mkdir(dst)
        
    labels = os.listdir(src)
    
    train_path = os.path.join(dst,'train')
    val_path = os.path.join(dst,'val')
    test_path = os.path.join(dst,'test')
    
    for path in [train_path, val_path, test_path]:
        if not os.path.exists(path): os.mkdir(path)
        for l in labels:
            if not os.path.exists(os.path.join(path, l)): os.mkdir(os.path.join(path, l))
    
    
    patients_N = sorted(list(set(i[:6] for i in os.listdir(os.path.join(src, 'N')))))
    patients_T = sorted(list(set(i[:6] for i in os.listdir(os.path.join(src, 'T')))))
    patients_P = sorted(list(set(i[:6] for i in os.listdir(os.path.join(src, 'P')))))
    
    random.seed(seed)
    
    random.shuffle(patients_N)
    random.shuffle(patients_T)
    random.shuffle(patients_P)
    
    train_patients = []
    val_patients = []
    test_patients = []
    
    for patients_set in [patients_N, patients_T, patients_P]:
        
        train_end = int(len(patients_set) * ratio[0])
        val_end = train_end + int(len(patients_set) * ratio[1])
        
        train_patients += patients_set[0:train_end]
        val_patients += patients_set[train_end:val_end]
        test_patients += patients_set[val_end:]
    
    sources = []
    destinations = []
    
    for l in labels:
        for img in os.listdir(os.path.join(src, l)):
            
            source = os.path.join(src,l)
            source = os.path.join(source,img)
            sources.append(source)
            
            if img[:6] in train_patients:    
                destination = os.path.join(train_path,l)
                destination = os.path.join(destination,img)

            elif img[:6] in val_patients: 
                destination = os.path.join(val_path,l)
                destination = os.path.join(destination,img)
            
            else:
                destination = os.path.join(test_path,l)
                destination = os.path.join(destination,img)
            
            destinations.append(destination)
    
    # implement multiprocessing to improve speed
    n = len(sources)//3
    s1 = sources[:n]
    s2 = sources[n:2*n]
    s3 = sources[2*n:]
    
    d1 = destinations[:n]
    d2 = destinations[n:2*n]
    d3 = destinations[2*n:]
    
    def f(S, D):
        for s,d in zip(S,D):
            shutil.copy(s, d)
    
    p1 = multiprocessing.Process(target=f, args=(s1,d1))
    p2 = multiprocessing.Process(target=f, args=(s2,d2))
    p3 = multiprocessing.Process(target=f, args=(s3,d3))

    p1.start()
    p2.start()
    p3.start()
    
    p1.join()
    p2.join()
    p3.join()