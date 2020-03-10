#Kevin Lee assign 8

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy.random as random
from datetime import datetime
file = "WabashRiver_DailyDischarge_20150317-20160324.txt"
data  = pd.read_csv(file,parse_dates=True, header=24, skiprows=[25], delimiter= '\t', index_col= ['datetime'])

# agency_cd	site_no	datetime	tz_cd	01_00060	01_00060_cd
#       agency_cd     site_no datetime tz_cd  01_00060 01_00060_cd
# USGS    3335500  2015-03-17    00:00   EST     23200           P
# USGS    3335500  2015-03-17    00:15   EST     23100           P
# USGS    3335500  2015-03-17    00:30   EST     23100           P

###################################
#DAILY Average for the entire data#
###################################
precip_daily = data.resample('D').mean()
# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(precip_daily.index.values,
           precip_daily['01_00060'],
           color='blue')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Discharge, cubic feet per second",
       title="Daily Average ")
plt.show()


###################################
#DAILY Average for top 10     data#
###################################

heightest=precip_daily.sort_values(by=['01_00060'], ascending=False)
heightest =  heightest.iloc[0:10]

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis 
ax.scatter(heightest.index.values,
           heightest['01_00060'],
           color='blue')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Discharge, cubic feet per second",
       title="Daily Average top 10")
plt.show()


#####################################
#Monthly Average for the entire data#
#####################################

# Resample to monthly precip sum and save as new dataframe
precip_monthly = precip_daily.resample('M').mean()

# Create figure and plot space
fig, ax = plt.subplots(figsize=(10, 10))

# Add x-axis and y-axis
ax.scatter(precip_monthly.index.values,
           precip_monthly['01_00060'],
           color='blue')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Discharge, cubic feet per second",
       title="Monthly Average ")

plt.show()