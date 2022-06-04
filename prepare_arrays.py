import geopandas as gpd
import rasterio as rio
import rasterio.plot
import matplotlib.pyplot as plt
import os

from PIL import Image

points = gpd.read_file("data/wyzyny_train.gpkg")
points['Y'] = points.centroid.x
points['X'] = points.centroid.y
if not os.path.exists("arrays"):
    os.makedirs("arrays")
with rio.open("data/Hillshade.tif") as hillshade:
    for x, y, index in zip(points.X, points.Y, range(0, points.shape[0])):
        px, py = hillshade.index(y, x)
        window = rio.windows.Window(py, px, 128, 128)
        clip = hillshade.read(1, window = window)
        # plt.imshow(clip, cmap='binary')
        # plt.show()
        clip = Image.fromarray(clip)
        clip.save(f"arrays/array{index}.png", format='PNG')


print(points)