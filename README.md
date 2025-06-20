# 🌍 Automatic Language Translation System with User Feedback

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-lightgrey)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

A web application that provides real-time language translation (English, French, Spanish, German) while learning from user corrections to improve accuracy.


## ✨ Features

- **AI-Powered Translations** using Hugging Face MarianMT
- **User Feedback System** (correct translations + 5-star ratings)
- **Translation History** with timestamps
- **Active Learning** - Improves based on user input
- **Responsive UI** works on mobile/desktop

## 🛠 Tech Stack

| Component       | Technology |
|----------------|------------|
| Frontend       | HTML5, CSS, Bootstrap |
| Backend        | Python Flask |
| AI Model       | Hugging Face Transformers (MarianMT) |
| Database       | SQLite (Flask-SQLAlchemy) |
| Deployment     | Docker (Optional) |

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip package manager
  
### Project Structure
translation-app/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── translation_service.py # AI translation logic
├── requirements.txt       # Dependencies
├── static/
│   └── css/
│       └── style.css      # Custom styles
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   └── history.html
└── instance/
    └── translations.db    # Database (ignored in .gitignore)
    
### Steps
1. Clone the repo:
   ```bash
   git clone https://github.com/abhijeet2028/translation-system.git
   cd translation-system
