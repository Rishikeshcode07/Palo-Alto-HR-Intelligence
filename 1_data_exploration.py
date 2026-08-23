import pandas as pd
import numpy as np
import os

# 1. Smartly find the dataset path (This will find the folder automatically )
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Palo Alto Networks.csv")

try:
    # 2. Load the dataset
    df = pd.read_csv(file_path)
    
    print("File successfully loaded!\n")
    print("--- Dataset Information ---")
    print(f"Total Rows: {df.shape[0]}")
    print(f"Total Columns Before Engineering: {df.shape[1]}")
    
    # 3. Check Attrition Distribution
    print("\n--- Attrition Count ---")
    print(df['Attrition'].value_counts())

    
    # STEP 2: FEATURE ENGINEERING (New Columns)
   
    
    # 1. Promotion Gap Ratio
    df['Promotion_Gap_Ratio'] = np.where(df['YearsAtCompany'] == 0, 0, 
                                         df['YearsSinceLastPromotion'] / df['YearsAtCompany'])

    # 2. Role Stagnation Index
    df['Role_Stagnation_Index'] = np.where(df['YearsAtCompany'] == 0, 0, 
                                           df['YearsInCurrentRole'] / df['YearsAtCompany'])

    # 3. Training Intensity Score
    df['Training_Intensity_Score'] = np.where(df['YearsAtCompany'] == 0, 0, 
                                              df['TrainingTimesLastYear'] / df['YearsAtCompany'])

    # 4. Manager Stability Indicator
    df['Manager_Stability_Indicator'] = np.where(df['YearsAtCompany'] == 0, 0, 
                                                 df['YearsWithCurrManager'] / df['YearsAtCompany'])

    print("\n--- After Feature Engineering ---")
    print(f"Total Columns Now: {df.shape[1]}")
    print("4 New Features added successfully!")
    
    # Display the new columns for the first 5 employees
    new_columns = ['Promotion_Gap_Ratio', 'Role_Stagnation_Index', 'Training_Intensity_Score', 'Manager_Stability_Indicator']
    print("\nSneak Peek of New Columns:")
    print(df[new_columns].head())

except FileNotFoundError:
    print("Error: Dataset still not found. Please check that 'Palo Alto Networks.csv' & '1_data_exploration.py' are in one folder only.")
    
