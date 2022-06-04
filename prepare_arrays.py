import geopandas as gpd
import rasterio as rio
import rasterio.plot
import matplotlib.pyplot as plt
import os

from PIL import Image

points = gpd.read_file("data/wyzyny_train.gpkg")
points['X'] = points.centroid.x
points['Y'] = points.centroid.y
if not os.path.exists("arrays"):
    os.makedirs("arrays")

with rio.open("data/Hillshade.tif") as hillshade:
    for x, y, index in zip(points.X, points.Y, range(0, points.shape[0])):
<<<<<<< HEAD
        px, py = hillshade.index(y, x)
        window = rio.windows.Window(py, px, 128, 128)
        clip = hillshade.read(1, window = window)
        # plt.imshow(clip, cmap='binary')
        # plt.show()
        clip = Image.fromarray(clip)
        clip.save(f"arrays/array{index}.png", format='PNG')
=======
        px, py = hillshade.index(x, y)
        window = rio.windows.Window(px, py, 128, 128)
        clip = hillshade.read(window = window)
        meta = hillshade.meta
        meta['width'], meta['height'] = 128, 128
        meta['transform'] = rio.windows.transform(window, hillshade.transform)
        with rio.open(f"arrays/array{index}.tif", 'w', **meta) as dst:
            dst.write(clip)
>>>>>>> be750e946e7c5ba5e68d019cdc29e9542dc7e34c

print(points)