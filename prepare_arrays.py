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

def clip_windows(file, type):
    points = gpd.read_file(file)
    src = rasterio.open('hillshade.tif') #raster
    i = 0
    for point in points['geometry']:
        x = point.xy[0][0]
        y = point.xy[1][0]
        row, col = src.index(x,y)
        rst = src.read(1, window=rasterio.windows.Window(col_off=col, row_off=row,
                                                        width=128, height=128))
        # plt.imshow(rst, cmap='binary')
        # plt.show()
        clip = Image.fromarray(rst)
        clip.save(f"arrays/{type}/array{i}.png", format='PNG')
        i=i+1

clip_windows("karpaty.gpkg", "mountains") #zbiory punktow
