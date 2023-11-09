# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:58:22 2023

@author: AJITH S
"""

import pandas as pd
import matplotlib.pyplot as plt
"""
The given line plot depicts the GDP per Capita from the year 2000 – 2020. 
The years are given on the x axis, while the GDP per Capita is in the y axis.....
"""
def create_line_graph(data, countries):
    filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2000) & (data['Year'] <= 2020)]
    plt.figure(figsize=(12, 6))
    for country in countries:
        country_data = filtered_data[filtered_data['Country'] == country]
        plt.plot(country_data['Year'], country_data['gdp_per_capita'], label=country)
    plt.xlabel('Year')
    plt.ylabel('gdp_per_capita')
    plt.title('GDP per capita from 2000-2020')
    plt.legend()
    plt.savefig('line_plot.png', dpi=300)
    plt.grid()
    plt.show()
"""
The given bar chart depicts the data to clean fuels for cooking from the year 2015 – 2020. 
The years are given on the x-axis and y-axis plots the access to clean fuels for cooking......
"""
def create_bar_graph(data, countries):
    filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2015) & (data['Year'] <= 2020)]
    grouped_data = filtered_data.groupby(['Year', 'Country'])['Access to clean fuels for cooking'].mean().unstack()
    ax = grouped_data.plot(kind='bar', figsize=(12, 4))
    plt.xlabel('Year')
    plt.ylabel('Access to clean fuels for cooking')
    plt.title('Access to clean fuels for cooking from 2015-2020')
    plt.legend(title='Country', loc='upper right')
    plt.savefig('bar_graph.png', dpi=300)
    plt.grid(axis='y')
    plt.show()
"""
The code reads a sustainable energy dataset and then concentrates on the variable
titled "Low-carbon electricity (%) electricity" for the years 2000 to 2020.....
"""
def create_pie_chart(data, countries):
    filtered_data = data[(data['Country'].isin(countries)) & (data['Year'] >= 2000) & (data['Year'] <= 2020)]
    grouped_data = filtered_data.groupby('Country')['Low-carbon electricity (% electricity)'].sum()
    plt.figure(figsize=(8, 8))
    plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Low-carbon electricity (% electricity) from 2000-2020')
    plt.savefig('pie_chart.png', dpi=300)
    plt.show()

def execute_all_graphs():
    data = pd.read_csv('global-data-on-sustainable-energy.csv')

    countries_line_graph = ['United States', 'Canada', 'Denmark', 'Germany', 'United Kingdom']
    create_line_graph(data, countries_line_graph)

    countries_bar_graph = ['Afghanistan', 'China', 'India']
    create_bar_graph(data, countries_bar_graph)

    countries_pie_chart = ['India', 'United Kingdom', 'United States', 'Brazil', 'Mexico', 'Australia']
    create_pie_chart(data, countries_pie_chart)

execute_all_graphs()