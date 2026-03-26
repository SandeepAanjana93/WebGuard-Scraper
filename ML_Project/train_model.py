# ================================
# Corporate HR Analytics ML Model
# ================================

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# ================================
# LOAD DATASET
# ================================
df = pd.read_csv("data.csv")

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# ================================
# DATA CLEANING
# ================================

# Remove unnecessary columns
drop_cols = ["EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"]
df.drop(columns=drop_cols, inplace=True)

# Convert target to numeric
df["Attrition"] = df["Attrition"].map({"Yes": 1, "No": 0})

# ================================
# ENCODE CATEGORICAL COLUMNS
# ================================
le = LabelEncoder()

cat_cols = df.select_dtypes(include="object").columns

for col in cat_cols:
    df[col] = le.fit_transform(df[col])

print("Categorical Encoding Done")

# ================================
# SPLIT FEATURES & TARGET
# ================================
X = df.drop("Attrition", axis=1)
y = df["Attrition"]

# Save feature column names (important for prediction)
joblib.dump(X.columns.tolist(), "model_features.pkl")

# ================================
# TRAIN TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# TRAIN MODEL
# ================================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

print("Model Training Completed")

# ================================
# MODEL EVALUATION
# ================================
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {acc*100:.2f}%")

print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ================================
# SAVE MODEL
# ================================
joblib.dump(model, "attrition_model.pkl")

print("\nModel Saved as attrition_model.pkl")
print("Feature list saved as model_features.pkl")