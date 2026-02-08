import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def check_missing_values(df):
    return df.isnull().sum()

def check_duplicates(df):
    return df.duplicated().sum()

def check_invalid_age(df):
    if 'age' in df.columns:
        return df[(df['age'] < 0) | (df['age'] > 120)]
    return pd.DataFrame()

def generate_report(df):
    print("📊 DATA QUALITY REPORT")
    print("-" * 30)

    missing = check_missing_values(df)
    duplicates = check_duplicates(df)
    invalid_age = check_invalid_age(df)

    print("\nMissing Values:")
    print(missing)

    print(f"\nDuplicate Rows: {duplicates}")

    if not invalid_age.empty:
        print("\nInvalid Age Records:")
        print(invalid_age)
    else:
        print("\nNo invalid age records found.")

def main():
    file_path = "data/sample_data.csv"
    df = load_data(file_path)
    generate_report(df)

if __name__ == "__main__":
    main()
