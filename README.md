# Agriculture-Drought-Analysis-using-time-series-satellite-data Using python

# What is drought?

Drought: Prolonged dry weather causing water scarcity, which can adversely affect agriculture, ecosystems, and human activities.

What is agriculture drought?

  Agricultural Drought: Prolonged dry weather with inadequate precipitation, leading to reduced crop yields, livestock losses, and negative impacts on agriculture.
  
  
  Agricultural drought, a common natural disaster in many regions, is a phenomenon that occurs when there is an extended period of inadequate soil moisture, leading to reduced crop growth and yield losses. Agricultural droughts have severe implications for farmers, rural communities, and global food security, as they can result in crop failure, reduced farm income, and increased vulnerability to poverty and hunger.
  
  
  Agricultural droughts are influenced by various factors, including climate variability, such as changes in precipitation patterns and temperature, as well as soil moisture dynamics and crop water requirements. Accurate prediction of agricultural drought is crucial for effective water resource management, crop planning, and risk mitigation strategies. Over the years, there have been significant advancements in remote sensing, climate modelling, and data analytics that have enabled the development of sophisticated techniques for agricultural drought analytics.

# For this project we used three major datasets.

NDVI, or Normalized Difference Vegetation Index, is a widely used remote sensing technique that measures the health and vitality of vegetation. It is calculated from satellite or aerial imagery by taking the normalized difference between near-infrared and red reflectance values. NDVI values range from -1 to 1, with higher values indicating denser and healthier vegetation cover. From them first one is NDVI (Normalized Difference Vegetation Index) derived from LANDSAT’s dataset from google earth engine of during kharif season means months are July,August,September from year 2014 to 2018 and 2020.


Satellite datasets for Land Surface Temperature (LST) provide valuable information on the thermal behaviour of the Earth's surface. These datasets are generated from thermal infrared sensors onboard satellites, which measure the emitted radiation from the land surface. Several satellite missions, such as MODIS, Landsat, and Sentinel, provide global or regional coverage of LST with different spatial and temporal resolutions.Second one is LST (Land Surface Temperature) which is derived from LANDSAT’s dataset from google earth engine by a script code of during kharif season means months are July, August, September from year 2014 to 2018 and 2020.


CHIRPS (Climate Hazards Group InfraRed Precipitation with Station data) is a widely used rainfall dataset that provides global precipitation information at high spatial and temporal resolutions. CHIRPS combines satellite- derived infrared measurements with ground-based precipitation data to estimate rainfall. It covers a historical period dating back to 1981 and is regularly updated. CHIRPS data is commonly used for monitoring and analysing precipitation patterns, drought assessment, flood prediction, crop monitoring, and climate research.And the third one is RAINFALL(Precipitation) which is also derived from CHIRP’S satellite data from google earth engine by a script code of during kharif season means months are July,August,September from year 2014 to 2018 and 2020.

#  Agricultural Drought Analytics Using DSI (Drought Severity Index) 
    DSI (Drought Severity Index) = (0.24*VCI) +(0.06*TCI) +(0.7*PCI)

    where
       VCI(Vegetation Condition Index) = ((NDVI - NDVImin) / (NDVImax - NDVImin)) x 100
       TCI(Temperature Condition Index ) = ((LSTmax - LST ) / (LSTmax - LSTmin)) x 100
       PCI (Precipitation condition index)=((RF - RFmin) / (RFmax - RFmin)) x 100
       
DSI(0 to 25) => severe drought 

DSI(25 to 50) => moderate drought 

DSI(>50) => no drought
