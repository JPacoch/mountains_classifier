import os
import numpy as np
from sklearn.model_selection import train_test_split
from random import sample
from PIL import Image

# przygotowanie struktury folderów
def prepare_dirs(dir):
    folders = [f"{dir}/train/mountains", f"{dir}/train/highlands", f"{dir}/test/mountains", f"{dir}/test/highlands"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"{folder} created")

prepare_dirs("data")

# wczytywanie tablic z folderu arrays
def read_arrays(type):
    list = []
    for file in os.listdir(os.getcwd() + f"\\arrays\\{type}"):
        print(os.path.join(os.getcwd() + f"\\arrays\\", file))
        img = Image.open(os.path.join(os.getcwd() + f"\\arrays\\{type}", file))
        arr = np.array(img)
        list.append(arr)
    return list

list = read_arrays("mountains")

# podział danych na zbiory i zapisanie w odpowiednich folderach
def split_and_save(list, type, ratio):
    assert ratio > 0 and ratio < 1, "Ratio must be in range (0,1)"
    assert type in ["mountains", "highlands"], "Type must be mountains or highlands"
    assert all(np.shape(i) == (128,128) for i in list), "All array must be of size (128, 128)"
    train, test, train_idx, test_idx = train_test_split(list, np.array(range(0, len(list))), train_size = ratio)
    print(f"{len(train)} / {len(test)}")

    for set, name, idxs in zip([train, test], ["train", "test"], [train_idx, test_idx]):
        path = os.getcwd() + "\\data\\" + name
        for arr, idx in zip(set, idxs):
            img = Image.fromarray(arr)
            img.save(path + f"\\{type}\\{type}{idx}.png", format='PNG')

split_and_save(list, "mountains", 0.7)
