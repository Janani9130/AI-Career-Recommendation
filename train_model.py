import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

# Load dataset
df = pd.read_csv("dataset/career_dataset.csv")

print("Dataset Loaded Successfully")
print(df.head())

# Features and target
X = df.drop("Career", axis=1)
y = df["Career"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
print("\nTraining Model...")
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:")
print(f"{accuracy * 100:.2f}%")

# Save model
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/career_model.pkl")

print("\nModel saved successfully!")