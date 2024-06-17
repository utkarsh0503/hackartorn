import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Dummy dataset
data = {
    'symptom1': [1, 0, 1, 0, 1],
    'symptom2': [0, 1, 0, 1, 1],
    'symptom3': [1, 1, 0, 0, 1],
    'disease': ['flu', 'cold', 'flu', 'cold', 'flu']
}

df = pd.DataFrame(data)

# Convert categorical data to numeric
df['disease'] = df['disease'].astype('category').cat.codes

# Features and labels
X = df[['symptom1', 'symptom2', 'symptom3']]
y = df['disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
with open('disease_predictor.pkl', 'wb') as file:
    pickle.dump(model, file)
