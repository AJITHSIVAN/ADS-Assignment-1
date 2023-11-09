# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 14:06:39 2023

@author: AJITH S
"""

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_dataset.csv' with the actual file path or URL of your dataset
data = pd.read_csv('global-data-on-sustainable-energy.csv')

# List of countries you want to filter
countries = ['United States', 'Canada', 'Denmark', 'Germany', 'United Kingdom']

# Filter the data for the specified countries and years
filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2000) & (data['Year'] <= 2020)]

# Create a line graph for each country
plt.figure(figsize=(12, 6))  # Set the figure size
for country in countries:
    country_data = filtered_data[filtered_data['Country'] == country]
    plt.plot(country_data['Year'], country_data['gdp_per_capita'], label=country)

# Set plot labels and legend
plt.xlabel('Year')
plt.ylabel('gdp_per_capita')
plt.title('gdp_per_capita from 2000-2020')
plt.legend()

# Save the plot to a PNG file
plt.savefig('line_plot.png', dpi=300)

# Show the plot
plt.grid()
plt.show()


""""Bar Graph"""

import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_dataset.csv' with the actual file path or URL of your dataset
data = pd.read_csv('global-data-on-sustainable-energy.csv')

# List of countries you want to filter
countries = ['Afghanistan', 'China', 'India']

# Filter the data for the specified countries and years
filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2015) & (data['Year'] <= 2020)]

# Group data by year and country to calculate the average life expectancy
grouped_data = filtered_data.groupby(['Year', 'Country'])['Access to clean fuels for cooking'].mean().unstack()

# Create a bar graph for each country
ax = grouped_data.plot(kind='bar', figsize=(12, 4))

# Set plot labels and legend
plt.xlabel('Year')
plt.ylabel('Access to clean fuels for cooking')
plt.title('Access to clean fuels for cooking from 2015-2020')
plt.legend(title='Country', loc='upper right')

# Save the plot to a PNG file
plt.savefig('bar_graph.png', dpi=300)

# Show the plot
plt.grid(axis='y')
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_dataset.csv' with the actual file path or URL of your dataset
data = pd.read_csv('global-data-on-sustainable-energy.csv')

# List of countries you want to filter
countries = ['India', 'United Kingdom', 'United States', 'Brazil', 'Mexico', 'Australia']

# Filter the data for the specified countries and years
filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2000) & (data['Year'] <= 2020)]

# Group data by country to calculate the total life expectancy
grouped_data = filtered_data.groupby('Country')['Low-carbon electricity (% electricity)'].sum()

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)

# Set plot title
plt.title('Low-carbon electricity (% electricity) from 2000-2020')






