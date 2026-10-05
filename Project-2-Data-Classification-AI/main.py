import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# 1. Load the dataset
iris = load_iris()

# 2. Create a DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# 3. Understand the dataset
print("=== DATASET INFORMATION ===")
print(f"Number of samples: {len(df)}")
print(f"Number of features: {len(iris.feature_names)}")

print("\nFirst 5 rows:")
print(df.head())

print("\nClass names:")
print(iris.target_names)

# 4. Separate features and target
X = df.drop("target", axis=1)
y = df["target"]

# 5. Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n=== DATA SPLIT ===")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# 6. Create the classification model
model = DecisionTreeClassifier(random_state=42)

# 7. Train the model
model.fit(X_train, y_train)

print("\n=== MODEL TRAINING ===")
print("Decision Tree model trained successfully.")

# 8. Make predictions
y_pred = model.predict(X_test)

# 9. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n=== MODEL RESULTS ===")
print(f"Accuracy: {accuracy * 100:.2f}%")

# 10. Test with new data
new_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names
)
prediction = model.predict(new_flower)

print("\n=== NEW PREDICTION ===")
print(f"Predicted class: {iris.target_names[prediction[0]]}")