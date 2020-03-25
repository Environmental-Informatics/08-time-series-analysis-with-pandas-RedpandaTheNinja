#KEvin Lee - assign 8 panda demo

import pandas as pd
import numpy as np
from pandas import Series, DataFrame, Panel
pd.set_option('display.max_rows',15) # this limit maximum numbers of rows

print("PANDA V:",pd.__version__)
# !wget http://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/monthly.ao.index.b50.current.ascii
ao = np.loadtxt('monthly.ao.index.b50.current.ascii')
print(ao[0:2])
print(ao.shape)
dates = pd.date_range('1950-01', periods=ao.shape[0], freq='M')
print(dates)
print(dates.shape)
AO = Series(ao[:,2], index=dates)
print(AO)

import matplotlib.pyplot as plt
# AO.plot()
# plt.show()

# AO['1980':'1990'].plot()
# plt.show()

# AO['1980-05':'1981-03'].plot()
# plt.show()

DayAO = AO.plot()
DayAO.set(xlabel="Year",
       ylabel="Oscillation Index",
       title="Daily Atlantic Oscillation AO")
DayAO.figure.savefig('Daily_AO.pdf')
plt.close()

print(AO[120])

print(AO['1960-01'])

print(AO['1960'])

print(AO[AO > 0])


#Create Series the same way as we did for AO:
nao = np.loadtxt('norm.nao.monthly.b5001.current.ascii')
dates_nao = pd.date_range('1950-01', periods=nao.shape[0], freq='M')
NAO = Series(nao[:,2], index=dates_nao)

print(NAO.index)

aonao = DataFrame({'AO' : AO, 'NAO' : NAO})
# aonao.plot(subplots=True)
# plt.show()

print(aonao.head())
print(aonao['NAO'])
print(aonao.NAO)

#diff
aonao['Diff'] = aonao['AO'] - aonao['NAO']
print(aonao.head())

#removing col
del aonao['Diff']
print(aonao.tail())

print(aonao['1981-01':'1981-03'])

import datetime
# aonao.loc[(aonao.AO > 0) & (aonao.NAO < 0) 
#         & (aonao.index > datetime.datetime(1980,1,1)) 
#         & (aonao.index < datetime.datetime(1989,1,1)),
#         'NAO'].plot(kind='barh')
# plt.show()

############################
#########STAT. ##############
###########################
print("Mean\n", aonao.mean())

print("Max\n",aonao.max())

print("Min\n", aonao.min())

print("MMean\n", aonao.mean(1))

print(aonao.describe())


#rolling stat 
AO_mm = AO.resample("A").mean()
# AO_mm.plot(style='g--')
# plt.show()

AO_mm = AO.resample("A").median()
MediMon=AO_mm.plot()
# plt.show()
MediMon.set(xlabel="Year",
       ylabel="Oscillation Index",
       title="Annual Median Atlantic Oscillation AO")
MediMon.figure.savefig('Annual_medi.pdf')
plt.close()

AO_mm = AO.resample("3A").apply(np.max)
# AO_mm.plot()
# plt.show()

AO_mm = AO.resample("A").apply(['mean', np.min, np.max])
# AO_mm['1900':'2020'].plot(subplots=True)
# AO_mm['1900':'2020'].plot()
# plt.show()

print(AO_mm)

rollilol= aonao.rolling(window=12, center=False).mean().plot()
rollilol.set(xlabel="Year",
       ylabel="Oscillation Index",
       title="Rolling Mean Atlantic Oscillation AO & NAO")
rollilol.figure.savefig('Rolling_mean.pdf')
plt.close()

# aonao.AO.rolling(window=120).corr(other=aonao.NAO).plot(style='-g')
# plt.show()

print(aonao.corr())