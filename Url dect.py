import re
import pandas as pd
import tldextract
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Function to extract features from URL
def extract_features(url):
    features = {
        "length": len(url),
        "num_digits": sum(c.isdigit() for c in url),
        "num_special_chars": len(re.findall(r"[!@#$%^&*(),.?\":{}|<>]", url)),
        "num_subdomains": len(tldextract.extract(url).subdomain.split('.')),
        "is_https": 1 if url.startswith("https") else 0
    }
    return features

# Example dataset (expand with real data)
data = {
    "url": ["https://secure-bank.com/login", "http://free-money.xyz", "https://paypal.com/signin"],
    "label": [0, 1, 0]  # 0 = Legit, 1 = Phishing
}

df = pd.DataFrame(data)
df_features = df["url"].apply(lambda x: extract_features(x)).apply(pd.Series)
X_train, X_test, y_train, y_test = train_test_split(df_features, df["label"], test_size=0.2, random_state=42)

# Train a RandomForest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test accuracy
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Function to predict phishing URLs
def predict_url(url):
    features = pd.DataFrame([extract_features(url)])
    prediction = model.predict(features)
    return "Phishing" if prediction[0] == 1 else "Legit"

# Example usage
test_url = "http://bank-login.secure-payment.com"
print(f"URL: {test_url} → {predict_url(test_url)}")
