#importing library
import pandas as pd
import numpy as np
import calendar
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

#importing data
df = pd.read_csv(r"C:\Users\gowda\oysisinfobyte\Unemployment_Rate_upto_11_2020.csv")

# Renaming columns for better clarity
df.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment Rate', 'Estimated Employed',
              'Estimated Labour Participation Rate', 'Region', 'longitude', 'latitude']

# Converting 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Converting 'Frequency' and 'Region' columns to categorical data type
df['Frequency'] = df['Frequency'].astype('category')
df['Region'] = df['Region'].astype('category')

# Extracting month from 'Date' and creating a 'Month' column
df['Month'] = df['Date'].dt.month

# Converting 'Month' to integer format
df['Month_int'] = df['Month'].apply(lambda x: int(x))

# Mapping integer month values to abbreviated month names
df['Month_name'] = df['Month_int'].apply(lambda x: calendar.month_abbr[x])

# Dropping the original 'Month' column
df.drop(columns='Month', inplace=True)

import plotly.express as px
fig = px.box(df, x='States', y='Estimated Unemployment Rate', color='States', title='Unemployment rate per States', template='seaborn')

fig.show()

plot_unemp = df[['Estimated Unemployment Rate','States']]
df_unemployed = plot_unemp.groupby('States').mean().reset_index()

df_unemployed = df_unemployed.sort_values('Estimated Unemployment Rate')

fig = px.bar(df_unemployed, x='States',y='Estimated Unemployment Rate',color = 'States',title = 'Average unemployment rate in each state',
             template='seaborn')
fig.show()

fig = px.bar(df, x='Region', y='Estimated Unemployment Rate', animation_frame='Month_name', color='States',
             title='Unemployment rate across regions from Jan. 2020 to Oct. 2020', height=700, template='seaborn')
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
fig.show()

# Creating a DataFrame with relevant columns
unemployed_df = df[['States', 'Region', 'Estimated Unemployment Rate', 'Estimated Employed', 'Estimated Labour Participation Rate']]

unemployed = unemployed_df.groupby(['Region', 'States'])['Estimated Unemployment Rate'].mean().reset_index()

# Creating a Sunburst chart 
fig = px.sunburst(unemployed, path=['Region', 'States'], values='Estimated Unemployment Rate', color_continuous_scale='rdylbu',
                  title='Unemployment rate in each Region and State', height=550, template='presentation')

fig.show()


import geopandas as gpd
import folium
from folium.plugins import HeatMap
m = folium.Map(location =[20.5937, 78.9629],tiles='openstreetmap',zoom_start=4.5)

HeatMap(data = df[['longitude', 'latitude']],radius = 50).add_to(m) 

m


# before the lockdown (January to March)
bf_lockdown = df[(df['Month_int'] >= 1) & (df['Month_int'] <4)]

# during the lockdown (April to July)
lockdown = df[(df['Month_int'] >= 4) & (df['Month_int'] <=7)]

# after the lockdown (August to October)
af_lockdown = df[(df['Month_int'] >7) & (df['Month_int'] <=10)]

# Calculating the mean unemployment rate before lockdown by state
m_bf_lock = bf_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()

# Calculating the mean unemployment rate during lockdown by state
m_lock = lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()

# Calculating the mean unemployment rate after lockdown by state
m_af_lock = af_lockdown.groupby('States')['Estimated Unemployment Rate'].mean().reset_index()

# Merge the DataFrames on the 'States' column
combined_mean_unemployment = m_bf_lock.merge(m_lock, on='States', suffixes=('_before', '_during'))
combined_mean_unemployment = combined_mean_unemployment.merge(m_af_lock, on='States', suffixes=('_during', '_after'))

# Rename columns for clarity
combined_mean_unemployment = combined_mean_unemployment.rename(columns={
    'Estimated Unemployment Rate_before': 'Before Lockdown',
    'Estimated Unemployment Rate_during': 'During Lockdown',
    'Estimated Unemployment Rate_after': 'After Lockdown'
})

# Display the combined DataFrame
combined_mean_unemployment.head()




# Sort the combined DataFrame by the "Mean Unemployment Rate Before Lockdown" 
combined_mean_unemployment_sorted = combined_mean_unemployment.sort_values(by='Before Lockdown',ascending=False)

print(combined_mean_unemployment_sorted.head())
print("\n")
print(combined_mean_unemployment_sorted.tail())

# Sort the combined DataFrame by the "Mean Unemployment Rate During Lockdown" column 
combined_mean_unemployment_sorted = combined_mean_unemployment.sort_values(by='During Lockdown',ascending=False)

print(combined_mean_unemployment_sorted.head())
print("\n")
print(combined_mean_unemployment_sorted.tail())

# Sort the combined DataFrame by the "Mean Unemployment Rate After Lockdown" column
combined_mean_unemployment_sorted = combined_mean_unemployment.sort_values(by='Estimated Unemployment Rate',ascending=False)

print(combined_mean_unemployment_sorted.head())
print("\n")
print(combined_mean_unemployment_sorted.tail())

# percentage change in unemployment rate

combined_mean_unemployment_sorted['Percentage change in Unemployment'] = (combined_mean_unemployment_sorted['During Lockdown'] - combined_mean_unemployment_sorted['Before Lockdown']/combined_mean_unemployment_sorted['Before Lockdown'])
plot_per = combined_mean_unemployment_sorted.sort_values('Percentage change in Unemployment')


# percentage change in unemployment during lockdown

fig = px.bar(plot_per, x='States',y='Percentage change in Unemployment',color='Percentage change in Unemployment',
            title='Percentage change in Unemployment in each state during lockdown',template='ggplot2')
fig.show()



# percentage change in unemployment rate

combined_mean_unemployment_sorted['Percentage change in Unemployment'] = (combined_mean_unemployment_sorted['Estimated Unemployment Rate'] - combined_mean_unemployment_sorted['Before Lockdown']/combined_mean_unemployment_sorted['Before Lockdown'])
plot_per = combined_mean_unemployment_sorted.sort_values('Percentage change in Unemployment')


# percentage change in unemployment after lockdown

fig = px.bar(plot_per, x='States',y='Percentage change in Unemployment',color='Percentage change in Unemployment',
            title='Percentage change in Unemployment in each state after lockdown',template='ggplot2')
fig.show()



# percentage change in unemployment rate

combined_mean_unemployment_sorted['Percentage change in Unemployment'] = (combined_mean_unemployment_sorted['Estimated Unemployment Rate'] - combined_mean_unemployment_sorted['During Lockdown']/combined_mean_unemployment_sorted['During Lockdown'])
plot_per = combined_mean_unemployment_sorted.sort_values('Percentage change in Unemployment')


# percentage change in unemployment after lockdown

fig = px.bar(plot_per, x='States',y='Percentage change in Unemployment',color='Percentage change in Unemployment',
            title='Percentage change in Unemployment in each state after lockdown',template='ggplot2')
fig.show()



