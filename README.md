# AI Customer Feedback Emotion Detector

This project uses IBM Watson NLP's emotion detection API to analyze the emotions present in customer feedback text. It is built using **Flask** for the backend and integrates a cloud-based service for emotion prediction.

---

##  Features

- Input text through a web interface.
- Detect emotions: **anger**, **disgust**, **fear**, **joy**, **sadness**.
- Returns the **dominant emotion**.
- Clean API design and modular backend structure.
- Static code analysis using `pylint` to ensure code quality.

---

##  Project Structure

```bash
AI-Customer-Feedback-Emotion-Detector/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py   # Main emotion analysis logic using IBM Watson API
│
├── static/
│   └── style.css              # Optional styling for web page
│
├── templates/
│   └── index.html             # Web interface for user input
│
├── server.py                  # Flask server with routes and logic
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation (this file)
