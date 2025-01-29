from preprocess import load_and_preprocess_data

# File path
file_path = r"C:\Users\HP\Desktop\Pharma-track-model\data\medicines.csv"

# Load data
X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess_data(file_path)

# ✅ Data loaded successfully
print("✅ Data Loaded Successfully!")
print("🔹 X_train shape:", X_train.shape)
print("🔹 y_train shape:", y_train.shape)

# 🔹 First 5 medicine names in training set
print("\n🔹 First 5 Medicines in Training Set:", vectorizer.inverse_transform(X_train)[:5])

# 🔹 First 5 substitute lists
print("\n🔹 First 5 Substitute Lists:\n", y_train.head())

