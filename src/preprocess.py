import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(file_path):
    # Load dataset with all values as strings
    df = pd.read_csv(file_path, dtype=str, low_memory=False)

    # Keep only necessary columns
    required_columns = ["name", "substitute0", "substitute1", "substitute2", "substitute3", "substitute4"]
    df = df[required_columns].dropna(subset=["name"])  # Drop rows where 'name' is missing

    # Fill NaN values in substitutes with empty strings
    df.fillna("", inplace=True)

    # Vectorize medicine names
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df["name"])  # Features (medicine names)
    
    # Prepare target variables (alternative medicines)
    y = df[["substitute0", "substitute1", "substitute2", "substitute3", "substitute4"]]

    # Split dataset into train & test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, vectorizer  # ✅ Returns exactly 5 values
