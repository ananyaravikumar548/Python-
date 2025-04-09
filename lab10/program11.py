import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load dataset
df = pd.read_csv('laptop.csv')

# --- Label Encoding for Storage column ---
le = LabelEncoder()
df['Storage_Encoded'] = le.fit_transform(df['Storage'])

# --- OneHot Encoding for Operating System column ---
ohe = OneHotEncoder(sparse=False, drop='first')  # drop='first' avoids dummy variable trap
os_encoded = ohe.fit_transform(df[['OperatingSystem']])

# Create DataFrame from OneHotEncoded values
os_encoded_df = pd.DataFrame(os_encoded, columns=ohe.get_feature_names_out(['OperatingSystem']))

# Combine all together
final_df = pd.concat([df, os_encoded_df], axis=1)

# Display final output
print("Original + Encoded Data:\n")
print(final_df)
