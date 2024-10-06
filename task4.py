import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/content/cleaned.csv'  # Replace with cleaned.csv if you want to use the other file
data = pd.read_csv(file_path)

# Display the first few rows to understand the structure of the dataset
print("First few rows of the dataset:")
print(data.head())

# Checking the columns of the dataset
print("\nColumns in the dataset:")
print(data.columns)

# 1. Visualizing accidents by road surface conditions
if 'Road_surface_conditions' in data.columns:
    road_surface_data = data['Road_surface_conditions'].value_counts()

    # Bar chart for road surface conditions
    plt.figure(figsize=(10, 6))
    road_surface_data.plot(kind='bar', color='skyblue')
    plt.title('Accidents by Road Surface Conditions')
    plt.xlabel('Road Surface Conditions')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart for road surface conditions
    plt.figure(figsize=(8, 8))
    plt.pie(road_surface_data, labels=road_surface_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Accidents by Road Surface Conditions')
    plt.show()
else:
    print("Column 'Road_surface_conditions' not found in the dataset.")

# 2. Visualizing accidents by weather conditions
if 'Weather_conditions' in data.columns:
    weather_conditions_data = data['Weather_conditions'].value_counts()

    # Bar chart for weather conditions
    plt.figure(figsize=(10, 6))
    weather_conditions_data.plot(kind='bar', color='lightgreen')
    plt.title('Accidents by Weather Conditions')
    plt.xlabel('Weather Conditions')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart for weather conditions
    plt.figure(figsize=(8, 8))
    plt.pie(weather_conditions_data, labels=weather_conditions_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Accidents by Weather Conditions')
    plt.show()
else:
    print("Column 'Weather_conditions' not found in the dataset.")

# 3. Visualizing accidents by light conditions
if 'Light_conditions' in data.columns:
    light_conditions_data = data['Light_conditions'].value_counts()

    # Bar chart for light conditions
    plt.figure(figsize=(10, 6))
    light_conditions_data.plot(kind='bar', color='salmon')
    plt.title('Accidents by Light Conditions')
    plt.xlabel('Light Conditions')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart for light conditions
    plt.figure(figsize=(8, 8))
    plt.pie(light_conditions_data, labels=light_conditions_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Accidents by Light Conditions')
    plt.show()
else:
    print("Column 'Light_conditions' not found in the dataset.")

# 4. Visualizing accident severity
if 'Accident_severity' in data.columns:
    accident_severity_data = data['Accident_severity'].value_counts()

    # Bar chart for accident severity
    plt.figure(figsize=(10, 6))
    accident_severity_data.plot(kind='bar', color='orange')
    plt.title('Accidents by Severity')
    plt.xlabel('Accident Severity')
    plt.ylabel('Number of Accidents')
    plt.xticks(rotation=45)
    plt.show()

    # Pie chart for accident severity
    plt.figure(figsize=(8, 8))
    plt.pie(accident_severity_data, labels=accident_severity_data.index, autopct='%1.1f%%', startangle=140)
    plt.title('Accidents by Severity')
    plt.show()
else:
    print("Column 'Accident_severity' not found in the dataset.")