import geopandas as gpd
import rasterio as rio
import rasterio.plot
import matplotlib.pyplot as plt
import os
from PIL import Image

# przygotowanie struktury folderów
def prepare_array_dirs():
    folders = [f"arrays/mountains", f"arrays/highlands"]
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"{folder} created")

prepare_array_dirs()

# wycinanie okien z punktów
def clip_windows(file, type):
    points = gpd.read_file(file)
    points['X'] = points.centroid.x
    points['Y'] = points.centroid.y
    with rio.open("data/Hillshade.tif") as hillshade:
        for x, y, index in zip(points.X, points.Y, range(0, points.shape[0])):
            px, py = hillshade.index(y, x)
            window = rio.windows.Window(py, px, 128, 128)
            clip = hillshade.read(1, window = window)
            # plt.imshow(clip, cmap='binary')
            # plt.show()
            clip = Image.fromarray(clip)
            clip.save(f"arrays/{type}/array{index}.png", format='PNG')

clip_windows("data/wyzyny_train.gpkg", "highlands")
