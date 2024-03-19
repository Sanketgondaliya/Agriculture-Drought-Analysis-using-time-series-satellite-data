# This script calculates and visualizes the Vegetation Condition Index (VCI)
# using the provided NDVI GeoTIFF file.
# The VCI is calculated using the following formula:
# VCI = (((vci_data - np.nanmin(vci_data))) / (np.nanmax(vci_data) - np.nanmin(vci_data)) * 100)
# The script also creates a corresponding VCI GeoTIFF file in the output directory specified.


import os
import rasterio
import numpy as np

import rasterio.mask
import numpy.ma as np_ma

#code for Temperature Condition Index
file_path = "D:/Eosproject/Eosproject/NDVI/2016.tif"

output_path = "D:/Eosproject/Eosproject/VCI"

with rasterio.open(file_path) as dataset:
    vci_data = dataset.read(1)
    vci_data[vci_data == 0] = np.nan
    vci_max = np.nanmax(vci_data)
    vci_min = np.nanmin(vci_data)
    vci = (((vci_data - np.nanmin(vci_data))) / (np.nanmax(vci_data) - np.nanmin(vci_data)) * 100)
    masked_data_v = np_ma.masked_invalid(vci)

    print("Maximum NDVI Value:", vci_max)
    print("Minimum NDVI Value:", vci_min)
    
    base_filename = os.path.basename(file_path)
    filename = os.path.splitext(base_filename)[0] + '_vci.tif'
    vci_file_path = os.path.join(output_path, filename)

    # Prepare metadata for the output file
    profile = dataset.profile
    profile.update(dtype=rasterio.float32)

    # Write the vCI values into a new GeoTIFF file
    with rasterio.open(vci_file_path, 'w', **profile) as dst:
        dst.write(masked_data_v.filled(np.nan).astype(rasterio.float32), 1)

    print("VCI GeoTIFF file has been created at:", vci_file_path)
    
import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.imshow(masked_data_v, cmap='viridis', interpolation='none', aspect='equal')
plt.colorbar(label='VCI Values')
plt.title('VCI MAP', fontsize=14)
plt.axis('on')
plt.show()