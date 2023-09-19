## Oysis-Infobyte-Task2
#UNEMPLOYMENT ANALYSIS WITH PYTHON

Unemployment is measured by the unemployment rate which is the number of people
who are unemployed as a percentage of the total labour force. We have seen a sharp
increase in the unemployment rate during Covid-19, so analyzing the unemployment rate
can be a good data science project. 

# Unemployment Rate Analysis in India

This project aims to analyze the unemployment rate in India from January 2020 to October 2020, with a focus on the impact of the COVID-19 lockdown. The data provides monthly estimates of unemployment rate, employed population, and labour participation rate for each state and region in India.

The project uses Python libraries such as pandas, numpy, matplotlib, seaborn, plotly, and folium to perform data manipulation, visualization, and exploration. The code is divided into several sections, each with a specific purpose and explanation.

## Importing library

This section imports the necessary libraries for the project.

## Importing data

This section imports the data from a CSV file and displays the first five rows of the data frame. The data has 10 columns:

- States: The name of the state in India
- Date: The date of the observation
- Frequency: The frequency of the observation (monthly)
- Estimated Unemployment Rate: The percentage of unemployed people in the labour force
- Estimated Employed: The number of employed people in millions
- Estimated Labour Participation Rate: The percentage of working-age population that is either employed or unemployed
- Region: The region of the state (North, South, East, West, Central, North-East)
- longitude: The longitude of the state
- latitude: The latitude of the state
- Month_int: The month of the observation as an integer

## Renaming columns for better clarity

This section renames some of the columns for better readability and consistency.

## Converting 'Date' column to datetime format

This section converts the 'Date' column from string to datetime format using pandas.

## Converting 'Frequency' and 'Region' columns to categorical data type

This section converts the 'Frequency' and 'Region' columns from object to categorical data type using pandas. This reduces the memory usage and improves the performance of the data frame.

## Extracting month from 'Date' and creating a 'Month' column

This section extracts the month from the 'Date' column and creates a new column called 'Month_int'.

## Converting 'Month' to integer format

This section converts the 'Month_int' column from float to integer format using pandas.

## Mapping integer month values to abbreviated month names

This section maps the integer month values to abbreviated month names using calendar library and creates a new column called 'Month_name'.

## Dropping the original 'Month' column

This section drops the original 'Month' column as it is no longer needed.

## Unemployment rate per States

This section creates a box plot using plotly library to visualize the distribution of unemployment rate per state. The plot shows that there is a large variation in unemployment rate across states, with some states having very high or low values.

## Average unemployment rate in each state

This section creates a bar plot using plotly library to visualize the average unemployment rate in each state. The plot shows that Haryana has the highest average unemployment rate, followed by Tripura and Rajasthan. Meghalaya has the lowest average unemployment rate, followed by Sikkim and Manipur.

## Unemployment rate across regions from Jan. 2020 to Oct. 2020

This section creates an animated bar plot using plotly library to visualize the unemployment rate across regions from January 2020 to October 2020. The plot shows that North region has the highest unemployment rate throughout the period, followed by Central region. South region has the lowest unemployment rate, followed by North-East region.

## Unemployment rate in each Region and State

This section creates a sunburst chart using plotly library to visualize the hierarchical relationship between region, state, and unemployment rate. The chart shows that North region has the highest share of unemployment rate, followed by Central region. Within each region, Haryana has the highest share of unemployment rate in North region, Madhya Pradesh has the highest share of unemployment rate in Central region, and so on.

## Heatmap of unemployment rate in India

This section creates a heatmap using folium library to visualize the spatial distribution of unemployment rate in India. The heatmap shows that states with higher latitude tend to have higher unemployment rate than states with lower latitude. There are also some hotspots of high unemployment rate in some states such as Haryana, Rajasthan, Bihar, Jharkhand, etc.

## Impact of lockdown on unemployment rate

This section analyzes the impact of lockdown on unemployment rate by dividing the data into three periods:

- Before lockdown (January to March)
- During lockdown (April to July)
- After lockdown (August to October)

The code calculates the mean unemployment rate for each period by state and merges them into one data frame. It also calculates the percentage change in unemployment rate during and after lockdown compared to before lockdown.

The code then creates three bar plots using plotly library to visualize:

- Percentage change in unemployment rate in each state during lockdown
- Percentage change in unemployment rate in each state after lockdown
- Percentage change in unemployment rate in each state after lockdown compared to during lockdown

The plots show that most states experienced a significant increase in unemployment rate during lockdown, with some states having more than 100% increase. After lockdown, most states experienced a decrease in unemployment rate, with some states having more than 50% decrease. However, some states still have higher unemployment rate after lockdown than before lockdown, such as Haryana, Tripura, Rajasthan, etc.
