import os
import fiona
import geopandas
import rasterio
import matplotlib.pyplot as plt

os.chdir('C:/Users/fujak/OneDrive/Pulpit/STUDIA/PROJEKT_SEKCJA')
os.getcwd()

karpaty = geopandas.read_file("Points/Mountains/karpaty.gpkg")
sudety = geopandas.read_file("Points/Mountains/sudety.gpkg")
wyzyny = geopandas.read_file("Points/Highlands/wyzyny_train.gpkg")
x = geopandas.read_file("glowne_obszary.gpkg")

gory = sudety.append(karpaty)

#hillshade = rio.open("data/Hillshade.tif")

rst = rasterio.open('hillshade.tif')
print(rst.bounds)
#red = rst.read(1)

fig, ax = plt.subplots()
ax.set_aspect('equal')
#ax.imshow(red)
#x.plot(ax=ax)
gory.plot(ax=ax, marker='o', color='red', markersize=5)
wyzyny.plot(ax=ax, marker='*', color='green', markersize=5)
plt.show()

#for i in gory:

#for i in wyzyny: