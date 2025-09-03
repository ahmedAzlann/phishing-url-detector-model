# 🛡️ Phishing URL Detection API

A Flask-based backend service to detect **phishing URLs** using multiple features such as WHOIS lookup, DNS checks, URL pattern analysis, and Google search results.

---

## 🚀 Features
- 🔍 Analyze any URL via a REST API (`/check`)
- 🌐 Extract URL features (length, digits, special characters, etc.)
- 📜 WHOIS & DNS-based domain checks
- ⏳ Domain age & expiry validation
- 📰 Website metadata scraping (title, description, keywords)
- 🤖 Ready for integration with ML-based phishing classifiers

---

## ⚙️ Tech Stack
- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Whois](https://pypi.org/project/python-whois/)
- [Google Search](https://pypi.org/project/googlesearch-python/)

---

## 📡 API Usage

### Endpoint
▶️ Getting Started
1. Clone the repository
git clone https://github.com/ahmedAzlann/phishing-url-detector-model.git
cd phishing-url-detection

2. Create a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask server
python app.py

🤝 Contributing

Contributions are welcome!

Fork the repo

Create a new branch (feature-xyz)

Commit changes

Open a Pull Request

📜 License

This project is licensed under the MIT License – feel free to use and modify.
