# This script calculates and visualizes the Drought Severity Index (DSI)
# using the VCI, TCI, and PCI GeoTIFF files provided.
# The DSI is calculated using the following formula:
# DSI = 0.24 * VCI + 0.06 * TCI + 0.7 * PCI
# The script also creates a corresponding Drought Severity GeoTIFF file
# in the output directory specified.

import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Define the paths for input VCI, TCI, and PCI GeoTIFF files
vci_file_path = 'D:/Eosproject/Eosproject/VCI/2014__vci.tif'
tci_file_path = 'D:/Eosproject/Eosproject/TCI/2014_tci.tif'
pci_file_path = 'D:/Eosproject/Eosproject/PCI/RAINFALL_2014_Kachh_pci.tif'
drought_severity_directory = 'D:/Eosproject/Eosproject/drought_severity_directory'

                                                                                                                               
# Open the VCI, TCI, and PCI files
with rasterio.open(vci_file_path) as vci_dataset, rasterio.open(tci_file_path) as tci_dataset, rasterio.open(pci_file_path) as pci_dataset:
    # Read the data
    vci_data = vci_dataset.read(1)
    tci_data = tci_dataset.read(1)
    pci_data = pci_dataset.read(1)
    
    # Replace all zero values with NaN values
    vci_data[vci_data == 0] = np.nan
    tci_data[tci_data == 0] = np.nan
    pci_data[pci_data == 0] = np.nan

    # Ensure all datasets have the same shape by cropping to the smallest common shape
    common_shape = (
        min(vci_data.shape[0], tci_data.shape[0], pci_data.shape[0]),
        min(vci_data.shape[1], tci_data.shape[1], pci_data.shape[1])
    )

    vci_data = vci_data[:common_shape[0], :common_shape[1]]
    tci_data = tci_data[:common_shape[0], :common_shape[1]]
    pci_data = pci_data[:common_shape[0], :common_shape[1]]

    # Calculate the Drought Severity layer based on the provided formula
    drought_severity = (0.24 * vci_data) + (0.06 * tci_data) + (0.7 * pci_data)

    # Create a corresponding Drought Severity GeoTIFF file
    base_filename = os.path.basename(vci_file_path)
    drought_severity_filename = os.path.splitext(base_filename)[0] + '_drought_severity.tif'
    drought_severity_file_path = os.path.join(drought_severity_directory, drought_severity_filename)

    # Use the common shape for the output file
    with rasterio.open(drought_severity_file_path, 'w', driver='GTiff', width=common_shape[1], height=common_shape[0], count=1, dtype=drought_severity.dtype, crs=vci_dataset.crs, transform=vci_dataset.transform) as dst:
        dst.write(drought_severity, 1)

#print("Drought Severity GeoTIFF file has been created.")
plt.figure(figsize=(8, 6))
plt.imshow(drought_severity, cmap='viridis', interpolation='none', aspect='equal')
plt.colorbar(label='DSI Values')
plt.title('DSI MAP', fontsize=14)
plt.axis('on')
plt.show()