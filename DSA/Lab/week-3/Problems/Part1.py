import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load the data set
data = pd.read_csv('population_by_country_2020.csv');

# prepare the data for plotting
countries = data['Country (or dependency)']
populations = data['Population (2020)']

# plot a bar chart
plt.figure(figsize=(20, 10))
plt.bar(countries, populations)
plt.xlabel('Countries')
plt.ylabel('Population (2020)')
plt.title('Population by Country')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()