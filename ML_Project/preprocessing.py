import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("data.csv")

# Remove unnecessary columns
df.drop(['EmployeeCount','EmployeeNumber','Over18','StandardHours'], axis=1, inplace=True)

# Convert Target column to numeric
df['Attrition'] = df['Attrition'].map({'Yes':1, 'No':0})

# Encode categorical columns
cat_cols = ['BusinessTravel','Department','EducationField','Gender',
            'JobRole','MaritalStatus','OverTime']

le = LabelEncoder()
for col in cat_cols:
    df[col] = le.fit_transform(df[col])

# Feature Scaling
scaler = StandardScaler()
num_cols = df.select_dtypes(include=['int64','float64']).columns
num_cols = num_cols.drop('Attrition')  # target ko scaling se bachao
df[num_cols] = scaler.fit_transform(df[num_cols])

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("Preprocessing Finished")