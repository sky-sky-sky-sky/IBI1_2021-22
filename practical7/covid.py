import os 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[9:19,[0,2]])#show the first and third columns from rows 10-20
b=list(covid_data.iloc[:,1])
c=list(covid_data.iloc[:,1])
d=list(covid_data.iloc[:,1])
for i in range(len(b)):
    if b[i]=='Afghanistan':
        b[i]=True
    else: 
        b[i]=False
print(covid_data.iloc[b,:])#use a Boolean to show “total cases” for all rows corresponding to Afghanistan. 
for i in range(len(c)):
    if c[i]=='China':
        c[i]=True
    else: 
        c[i]=False
china_dates=covid_data.iloc[c,0]
china_new_cases=covid_data.iloc[c,2]
china_new_deaths=covid_data.iloc[c,3]
print('the mean of china_new_cases is',np.mean(china_new_cases),'\n','the mean of china_new_deaths is',np.mean(china_new_deaths))#compute the mean number of new cases and new deaths in China and print.
for i in range(len(d)):
    if d[i]=='Russia':
        d[i]=True
    else: 
        d[i]=False
Russia_dates=covid_data.iloc[d,0]
Russia_new_cases=covid_data.iloc[d,2]
Russia_new_deaths=covid_data.iloc[d,3]
fig=plt.figure()
pl1=fig.add_subplot(231)
plt.boxplot(china_new_cases)
plt.title('china_new_cases')
plt.ylabel("number")
pl2=fig.add_subplot(232)
plt.boxplot(china_new_deaths)
plt.title('china_new_deaths')#create a boxplot of new cases and new deaths in China worldwide. 
plt.ylabel("number")
pl3=fig.add_subplot(233)
plt.plot(china_dates, china_new_cases,color='b')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-45)
plt.title('total cases in China')
plt.ylabel("number")
plt.xlabel("date")
pl3=fig.add_subplot(234)
plt.plot(china_dates, china_new_deaths,color='r')
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-45)
plt.title('total deaths in China')
plt.ylabel("number")
plt.xlabel("date")#plot both new cases and new deaths in China over time. 
pl3=fig.add_subplot(235)
plt.plot(Russia_dates, Russia_new_cases,color='b')
plt.xticks(Russia_dates.iloc[0:len(Russia_dates):4],rotation=-45)
plt.title('total cases in Russia')
plt.ylabel("number")
plt.xlabel("date")
pl3=fig.add_subplot(236)
plt.plot(Russia_dates, Russia_new_deaths,color='r')
plt.xticks(Russia_dates.iloc[0:len(Russia_dates):4],rotation=-45)
plt.title('total deaths in Russia')
plt.ylabel("number")
plt.xlabel("date")# There is code to answer the question stated in file question.txt 
plt.show()


