import pandas as pd
import numpy as np
import os
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Load Data
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Palo Alto Networks.csv")
df = pd.read_csv(file_path)

# 2. Feature Engineering
df['Promotion_Gap_Ratio'] = np.where(df['YearsAtCompany'] == 0, 0, df['YearsSinceLastPromotion'] / df['YearsAtCompany'])
df['Role_Stagnation_Index'] = np.where(df['YearsAtCompany'] == 0, 0, df['YearsInCurrentRole'] / df['YearsAtCompany'])
df['Training_Intensity_Score'] = np.where(df['YearsAtCompany'] == 0, 0, df['TrainingTimesLastYear'] / df['YearsAtCompany'])
df['Manager_Stability_Indicator'] = np.where(df['YearsAtCompany'] == 0, 0, df['YearsWithCurrManager'] / df['YearsAtCompany'])

print("Data loaded & Features created...")

# 3. Data Preprocessing & Scaling
clustering_features = [
    'Promotion_Gap_Ratio', 
    'Role_Stagnation_Index', 
    'Training_Intensity_Score', 
    'Manager_Stability_Indicator', 
    'YearsAtCompany', 
    'TotalWorkingYears'
]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[clustering_features])
print("Data scaling successful...")

# 4. K-Means Clustering (4 Clusters)
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['Career_Cluster'] = kmeans.fit_predict(scaled_data)

# Cluster Labels Mapping based on Data Characteristics
cluster_names = {
    0: 'Long-term Contributors / Senior Staff',
    1: 'Promotion-Stalled / Stagnant Profiles',
    2: 'Steady Performers / Fast-Trackers',
    3: 'Early-Career Explorers / New Joiners'
}
df['Cluster_Name'] = df['Career_Cluster'].map(cluster_names)

print("\n K-Means Clustering Successful!")
print("--- Employee Distribution across Clusters ---")
print(df['Cluster_Name'].value_counts())

# 5. Fixed Risk Scoring using pd.cut
bins = [-0.01, 0.0, 0.35, 1.01]
labels = ['Low', 'Medium', 'High']
df['Promotion_Gap_Risk'] = pd.cut(df['Promotion_Gap_Ratio'], bins=bins, labels=labels)

print("\n--- Promotion Gap Risk Distribution ---")
print(df['Promotion_Gap_Risk'].value_counts())

# 6. Retention Opportunity Identification
# (Employees with High Stagnation / Gap Risk but not yet quit)
df['Retention_Opportunity'] = np.where(
    (df['Attrition'] == 0) & (df['Promotion_Gap_Risk'] == 'High'), 'High Priority', 'Standard'
)

# 7. Save Processed Data
output_path = os.path.join(script_dir, "Processed_HR_Data.csv")
df.to_csv(output_path, index=False)
print(f"\n Success! File saved at:\n{output_path}")