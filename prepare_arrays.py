import geopandas as gpd
import rasterio as rio
import rasterio.plot
import matplotlib.pyplot as plt
import os

points = gpd.read_file("data/wyzyny_train.gpkg")
points['Y'] = points.centroid.x
points['X'] = points.centroid.y
if not os.path.exists("arrays"):
    os.makedirs("arrays")
with rio.open("data/Hillshade.tif") as hillshade:
    for x, y, index in zip(points.X, points.Y, range(0, points.shape[0])):
        px, py = hillshade.index(x, y)
        window = rio.windows.Window(px, py, 128, 128)
        clip = hillshade.read(1, window = window)
        meta = hillshade.meta
        meta['width'], meta['height'] = 128, 128
        meta['transform'] = rio.windows.transform(window, hillshade.transform)
        with rio.open(f"arrays/array{index}.tif", 'w', **meta) as dst:
            dst.write(clip)


print(points)