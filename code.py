# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 13:50:08 2023

@author: AJITH S
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data
file_path = "global-data-on-sustainable-energy.csv"
data = pd.read_csv(file_path)

# Extract data for specific countries (e.g., Yemen, Zambia, Zimbabwe)
yemen_data = data[data['Country'] == 'Yemen']
zambia_data = data[data['Country'] == 'Zambia']
zimbabwe_data = data[data['Country'] == 'Zimbabwe']

# Line Plot
plt.figure(figsize=(10, 6))
plt.plot(yemen_data['Year'], yemen_data['Energy_Consumption'], label='Yemen')
plt.plot(zambia_data['Year'], zambia_data['Energy_Consumption'], label='Zambia')
plt.plot(zimbabwe_data['Year'], zimbabwe_data['Energy_Consumption'], label='Zimbabwe')
plt.xlabel('Year')
plt.ylabel('Energy Consumption')
plt.title('Energy Consumption Over Years for Yemen, Zambia, and Zimbabwe')
plt.legend()
plt.show()

# Bar Chart
plt.figure(figsize=(10, 6))
plt.bar('Yemen', yemen_data['Energy_Consumption'].sum(), label='Yemen')
plt.bar('Zambia', zambia_data['Energy_Consumption'].sum(), label='Zambia')
plt.bar('Zimbabwe', zimbabwe_data['Energy_Consumption'].sum(), label='Zimbabwe')
plt.xlabel('Country')
plt.ylabel('Total Energy Consumption')
plt.title('Total Energy Consumption for Yemen, Zambia, and Zimbabwe in a Specific Year')
plt.legend()
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(yemen_data['GDP'], yemen_data['Energy_Consumption'], label='Yemen')
plt.scatter(zambia_data['GDP'], zambia_data['Energy_Consumption'], label='Zambia')
plt.scatter(zimbabwe_data['GDP'], zimbabwe_data['Energy_Consumption'], label='Zimbabwe')
plt.xlabel('GDP')
plt.ylabel('Energy Consumption')
plt.title('Scatter Plot of GDP vs Energy Consumption for Yemen, Zambia, and Zimbabwe')
plt.legend()
plt.show()