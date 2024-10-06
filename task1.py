import pandas as pd
import matplotlib.pyplot as plt

# Load the main population data file
data_file = '/content/API_SP.POP.TOTL_DS2_en_csv_v2_31753.csv'
df = pd.read_csv(data_file, skiprows=4)

# Check the first few rows to understand the structure
print(df.head())

# Selecting a year (e.g., 2022) for population data
# Make sure that the year exists in the data. Replace "2022" with the appropriate column if needed.
year = '2022'
df_plot = df[['Country Name', year]].dropna()

# Sort by population for better visualization
df_plot = df_plot.sort_values(by=year, ascending=False).head(10)  # Top 10 countries

# Plotting the bar graph for the top 10 most populated countries
plt.figure(figsize=(10,6))
plt.bar(df_plot['Country Name'], df_plot[year], color='skyblue')
plt.xlabel('Country')
plt.ylabel(f'Population in {year}')
plt.xticks(rotation=90)
plt.title(f'Top 10 Populated Countries in {year}')
plt.tight_layout()

# Show the plot
plt.show()
