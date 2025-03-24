**🛡️ CyberSecurity Tools: Keylogger Detector & Phishing URL Classifier**

🚀 Overview

This repository contains two cybersecurity tools designed to enhance security awareness and protection:

🔑 Keylogger Detector: Scans running processes, registry entries, and network traffic for keylogger behavior.

🌐 Phishing URL Detector: Uses machine learning to classify URLs as phishing or legitimate based on URL patterns.

**1️⃣ Keylogger Detector**

🔍 Features:

✅ Scans system processes for suspicious activity.
✅ Detects registry modifications by potential keyloggers.
✅ Monitors network activity for data exfiltration.

⚙️ Installation & Usage:

cd Keylogger-Detector

pip install -r requirements.txt

python keylogger_detector.py

**2️⃣ Phishing URL Detector**

🛡️ Features:

✅ Extracts multiple features from URLs (length, special characters, subdomains, HTTPS presence, WHOIS domain age).
✅ Uses a machine learning model (Random Forest) for classification.
✅ Trains on a sample dataset and predicts phishing websites.

⚙️ Installation & Usage:

cd Phishing-URL-Detector

pip install -r requirements.txt

python phishing_detector.py
