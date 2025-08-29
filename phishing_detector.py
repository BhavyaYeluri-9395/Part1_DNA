import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load dataset
data = pd.read_csv("phishing-detector/data/urls.csv")
# 2. Split features & target
X = data.drop(columns=["Result", "URL"])
y = data["Result"]

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Test model
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 6. Save model
joblib.dump(model, "phishing_model.pkl")
print("✅ Model saved as phishing_model.pkl")
