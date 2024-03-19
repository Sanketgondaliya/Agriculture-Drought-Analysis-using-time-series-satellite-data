import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import rasterio.mask
import numpy.ma as np_ma


#code for Temperature Condition Index
file_path = "D:/Eosproject/Eosproject/LST/2014.tif"

output_path = "D:/Eosproject/Eosproject/TCI"

with rasterio.open(file_path) as dataset:
    tci_data = dataset.read(1)
    tci_data[tci_data == 0] = np.nan
    tci_max = np.nanmax(tci_data)
    tci_min = np.nanmin(tci_data)
    tci = (((np.nanmax(tci_data) - tci_data)) / (np.nanmax(tci_data) - np.nanmin(tci_data)) * 100)
    masked_data = np_ma.masked_invalid(tci)

    print("Maximum LST Value:", tci_max)
    print("Minimum LST Value:", tci_min)

    # Create a corresponding TCI GeoTIFF file
    base_filename = os.path.basename(file_path)
    filename = os.path.splitext(base_filename)[0] + '_tci.tif'
    tci_file_path = os.path.join(output_path, filename)

    # Prepare metadata for the output file
    profile = dataset.profile
    profile.update(dtype=rasterio.float32)

    # Write the TCI values into a new GeoTIFF file
    with rasterio.open(tci_file_path, 'w', **profile) as dst:
        dst.write(masked_data.filled(np.nan).astype(rasterio.float32), 1)

    print("TCI GeoTIFF file has been created at:", tci_file_path)

plt.figure(figsize=(8, 6))
plt.imshow(masked_data, cmap='viridis', interpolation='none', aspect='equal')
plt.colorbar(label='TCI Values')
plt.title('TCI MAP', fontsize=14)
plt.axis('on')
plt.show()
