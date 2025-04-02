import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, MinMaxScaler,␣
↪StandardScaler
# Load dataset
df = pd.read_csv("data.csv")
print(df)
