import joblib
import pandas as pd

# Load trained model
model = joblib.load("phishing_model.pkl")

# Example new data (same features as training, without Result & URL)
new_sites = pd.DataFrame([
    [0, 0, 0, 0, 0, 1, 1, 0],  # Example legit
    [1, 1, 0, 1, 1, 3, 0, 1]   # Example phishing
], columns=["Having_IP","URL_Length","Shortening_Service","Has_At_Symbol","Prefix_Suffix","Subdomain_Count","SSLfinal_State","HTTPS_Token"])

# Predict
predictions = model.predict(new_sites)

for i, pred in enumerate(predictions):
    if pred == 1:
        print(f"Site {i+1}: ✅ Legitimate")
    else:
        print(f"Site {i+1}: ⚠️ Phishing")
