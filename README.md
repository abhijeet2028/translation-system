# 🌐 AI-Powered Language Translator with Feedback Loop

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.x-red?logo=flask)](https://flask.palletsprojects.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow)](https://huggingface.co/)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/repo-name?style=social)](https://github.com/your-username/repo-name)

<div align="center">
  <img src="https://i.imgur.com/JQ9w5Bn.gif" width="800" alt="Demo GIF">
</div>

## 📌 Overview
An intelligent translation system that:
- Translates between **English, French, Spanish, and German** using MarianMT
- **Learns from user corrections** to improve future translations
- Stores history with **interactive feedback mechanism**
- Built with scalability in mind for adding new languages

## ✨ Key Features
| Feature | Description |
|---------|-------------|
| **Real-time Translation** | Powered by Hugging Face's MarianMT models |
| **Feedback Integration** | Users can correct translations and rate accuracy (1-5 stars) |
| **Active Learning** | System improves using collected feedback data |
| **History Tracking** | View/export past translations with filters |
| **Responsive UI** | Works on mobile, tablet, and desktop |

## 🛠 Tech Stack
```mermaid
pie
    title Technology Stack
    "Flask (Python)" : 35
    "HuggingFace Transformers" : 30
    "SQLite" : 20
    "HTML/CSS/JS" : 15
### Steps
1. Clone the repo:
   ```bash
   git clone https://github.com/abhijeet2028/translation-system.git
   cd translation-system
