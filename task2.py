# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the datasets
train_file_path = '/content/train.csv'  # Replace with the correct path in Colab if needed
test_file_path = '/content/test.csv'
gender_submission_file_path = '/content/gender_submission.csv'

train_data = pd.read_csv(train_file_path)
test_data = pd.read_csv(test_file_path)
gender_submission_data = pd.read_csv(gender_submission_file_path)

# Display the first few rows of the training dataset
print("First few rows of the training dataset:")
print(train_data.head())

# Display the summary of the dataset
print("\nSummary of the dataset:")
print(train_data.info())

# Check for missing values in the dataset
print("\nMissing values in each column:")
print(train_data.isnull().sum())

# Data Cleaning - Handling Missing Values
# Fill missing 'Age' with the median age
train_data['Age'].fillna(train_data['Age'].median(), inplace=True)

# Fill missing 'Embarked' with the most common value (mode)
train_data['Embarked'].fillna(train_data['Embarked'].mode()[0], inplace=True)

# Drop the 'Cabin' column due to too many missing values
train_data.drop(columns=['Cabin'], inplace=True)

# Verify if missing values are handled
print("\nMissing values after cleaning:")
print(train_data.isnull().sum())

# EDA - Exploratory Data Analysis

# 1. Distribution of the target variable - Survival rate
plt.figure(figsize=(6, 4))
sns.countplot(data=train_data, x='Survived')
plt.title('Survival Count')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# 2. Distribution of passenger classes
plt.figure(figsize=(6, 4))
sns.countplot(data=train_data, x='Pclass', hue='Survived')
plt.title('Survival by Passenger Class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()

# 3. Distribution of Age
plt.figure(figsize=(8, 6))
sns.histplot(train_data['Age'], kde=True, bins=30)
plt.title('Age Distribution of Passengers')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 4. Survival rate based on Age
plt.figure(figsize=(8, 6))
sns.histplot(train_data[train_data['Survived'] == 1]['Age'], color='green', kde=True, bins=30, label='Survived')
sns.histplot(train_data[train_data['Survived'] == 0]['Age'], color='red', kde=True, bins=30, label='Not Survived')
plt.legend()
plt.title('Survival Distribution Based on Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# 5. Survival rate based on Sex
plt.figure(figsize=(6, 4))
sns.countplot(data=train_data, x='Sex', hue='Survived')
plt.title('Survival by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 6. Correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(train_data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Titanic Dataset')
plt.show()

# 7. Survival rate based on Embarked location
plt.figure(figsize=(6, 4))
sns.countplot(data=train_data, x='Embarked', hue='Survived')
plt.title('Survival by Embarked Location')
plt.xlabel('Embarked Location')
plt.ylabel('Count')
plt.show()

# 8. Pairplot to explore relationships between features
sns.pairplot(train_data[['Survived', 'Age', 'Fare', 'Pclass', 'SibSp', 'Parch']], hue='Survived', diag_kind='kde')
plt.show()
