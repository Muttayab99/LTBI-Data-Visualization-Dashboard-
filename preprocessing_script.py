import pandas as pd

def impute_data(input_file, output_file):
    # Read the CSV file into a DataFrame
    try:
        data = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    if data.empty:
        print("Error: Dataset is empty!")
        return

    # Impute missing values
    for column in data.columns:
        if data[column].dtype in ['float64', 'int64']:  # Numerical columns
            mean_value = data[column].mean(skipna=True)
            data[column].fillna(mean_value, inplace=True)
        else:  # Categorical columns
            mode_value = data[column].mode().iloc[0] if not data[column].mode().empty else None
            data[column].fillna(mode_value, inplace=True)

    # Save the processed DataFrame to a new CSV file
    data.to_csv(output_file, index=False)
    print(f"Imputation complete. Output written to '{output_file}'.")

# Define input and output file names
input_file = "LTBI_estimates_cleaned.csv"
output_file = "processed_LTBI_dataset.csv"

# Perform imputation
impute_data(input_file, output_file)
