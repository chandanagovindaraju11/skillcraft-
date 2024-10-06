import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load the dataset
file_path = 'content/bank-additional.csv'  # Update the path accordingly
data = pd.read_csv(file_path, delimiter=';')

# Preprocessing: Encoding categorical variables
label_encoders = {}
for column in data.select_dtypes(include=['object']).columns:
    if column != 'y':  # Skip the target variable for now
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

# Encode target variable 'y'
data['y'] = LabelEncoder().fit_transform(data['y'])

# Split the data into features and target
X = data.drop(columns=['y'])
y = data['y']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Build and train the decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Print classification report
print(classification_report(y_test, y_pred, target_names=['no', 'yes']))
