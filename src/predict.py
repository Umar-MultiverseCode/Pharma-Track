import pandas as pd

# Load CSV containing medicine names and substitutes
file_path = r"C:\Users\HP\Desktop\Pharma-track-model\data\medicines.csv"
df = pd.read_csv(file_path, dtype=str).fillna("")  # Fill NaN values with empty string

def get_alternative_medicines(medicine_name):
    """
    Returns a list of alternative medicines for a given medicine name.
    """
    # Convert user input to lowercase for case-insensitive matching
    medicine_name = medicine_name.lower()

    # Search for the medicine in the dataframe
    match = df[df["name"].str.lower() == medicine_name]

    if match.empty:
        return f"No alternatives found for '{medicine_name}'. Please check the spelling."

    # Extract only substitute columns (ignore other columns like side effects, class, etc.)
    substitute_columns = [col for col in df.columns if "substitute" in col]
    substitutes = match.iloc[0][substitute_columns].values  # Extract substitute values
    substitutes = [s for s in substitutes if s]  # Remove empty values

    if not substitutes:
        return f"No substitutes available for '{medicine_name}'."

    return substitutes

if __name__ == "__main__":
    user_input = input("\n🔍 Enter Medicine Name: ")
    alternatives = get_alternative_medicines(user_input)

    if isinstance(alternatives, list):
        print(f"\n✅ Alternatives for '{user_input}':\n")
        for idx, alt in enumerate(alternatives, start=1):
            print(f"  {idx}. {alt}")  # Numbered format
    else:
        print(alternatives)
