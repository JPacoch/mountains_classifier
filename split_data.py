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

prepare_dirs("dane")

# generowanie sztucznych tablic do testów
list = []
for i in range(0, 50):
    arr = np.random.randint(256, size = (128, 128))
    list.append(arr)

# podział danych na zbiory i zapisanie w odpowiednich folderach
def split_and_save(list, type, ratio):
    assert ratio > 0 and ratio < 1, "Ratio must be in range (0,1)"
    assert type in ["mountains", "highlands"], "Type must be mountains or highlands"
    train, test, train_idx, test_idx = train_test_split(list, np.array(range(0, len(list))), train_size = ratio)
    print(f"{len(train)} / {len(test)}")

    for set, name, idxs in zip([train, test], ["train", "test"], [train_idx, test_idx]):
        path = os.getcwd() + "\\dane\\" + name
        for arr, idx in zip(set, idxs):
            img = Image.fromarray(arr)
            img.save(path + f"\\{type}\\{type}{idx}.png")

split_and_save(list, "mountains", 0.7)