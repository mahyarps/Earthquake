"""
The goal of this project is to show a graph which shows lists for each decade
corresponding number of earthquakes categorized by the strength of their
magnitude as Extreme, Medium, or Strong.
"""

import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt

# Save all data from "database.csv" file to a DataFrame.
data = pd.read_csv('database.csv')
# Conver the date column to the parser date and save all years inside "year" DataFrame.
year = pd.read_csv('database.csv', converters={0: lambda x: parser.parse(x).year}, usecols=[0])


def Magnitude_desc(magnitude_df):
    """
    Categorize earthquakes by strength of their magnitude as Extreme,
    Medium or Strong.
    """
    eq_magnitude = pd.cut(magnitude_df, [0, 6.5, 7.5, data['Magnitude'].max()],
                                         labels=['Medium', 'Strong', 'Extreme'])
    return eq_magnitude


# Convert year to Decade and add them to the "data" DataFrame.
data['Decade'] = year['Date'].apply(lambda x: 10*(x // 10))
# Add the earthquakes magnitude array list to the "data" DataFrame.
data['Magnitude_desc'] = Magnitude_desc(data['Magnitude'])

# Group by datas by magnitude and decade and plot the number of earthquakes
# per each decade.
data.pivot_table('Magnitude', index='Decade', columns='Magnitude_desc', aggfunc='count').plot()
plt.title('Number of earthquakes per decade')
plt.ylabel('Number of Earthquakes')
plt.xlabel('Decade')
data.pivot_table('Magnitude', index='Decade', columns='Magnitude_desc', aggfunc='count').plot.bar()
plt.title('Number of earthquakes per decade')
plt.ylabel('Number of Earthquakes')
plt.xlabel('Decade')
