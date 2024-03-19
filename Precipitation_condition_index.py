import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import rasterio.mask
import numpy.ma as np_ma

file_path = "D:/Eosproject/Eosproject/RAINFALL/RAINFALL_2014_Kachh.tif"

output_path = "D:/Eosproject/Eosproject/PCI"

with rasterio.open(file_path) as dataset:
    pci_data = dataset.read(1)
    pci_data[pci_data == 0] = np.nan
    pci_max = np.nanmax(pci_data)
    pci_min = np.nanmin(pci_data)
    pci = (((pci_data - np.nanmin(pci_data))) / (np.nanmax(pci_data) - np.nanmin(pci_data)) * 100)
    masked_data_p = np_ma.masked_invalid(pci)

    print("Maximum PCI Value:", pci_max)
    print("Minimum PCI Value:", pci_min)

    base_filename = os.path.basename(file_path)
    filename = os.path.splitext(base_filename)[0] + '_pci.tif'
    pci_file_path = os.path.join(output_path, filename)

    # Prepare metadata for the output file
    profile = dataset.profile
    profile.update(dtype=rasterio.float32)

    # Write the PCI values into a new GeoTIFF file
    with rasterio.open(pci_file_path, 'w', **profile) as dst:
        dst.write(masked_data_p.filled(np.nan).astype(rasterio.float32), 1)

    print("PCI GeoTIFF file has been created at:", pci_file_path)
    
plt.figure(figsize=(8, 6))
plt.imshow(masked_data_p, cmap='viridis', interpolation='none', aspect='equal')
plt.colorbar(label='PCI Values')
plt.title('PCI MAP', fontsize=14)
plt.axis('on')
plt.show()