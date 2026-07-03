# # 📧 Email Spam Detection using Machine Learning

A Machine Learning web application that classifies email or SMS messages as **Spam** or **Not Spam (Ham)** using Natural Language Processing (NLP). The application is built with **Python**, **Scikit-learn**, and **Streamlit**, providing a fast and interactive interface for real-time spam detection.

## 🌐 Live Demo

🚀 **Try the application here:**
https://emailspamdetectionbysachin.streamlit.app/

## 📂 GitHub Repository

🔗 https://github.com/sachin-418/Email_spam_detection

---

## 📖 Project Overview

Spam messages are one of the most common problems in digital communication. This project uses Natural Language Processing (NLP) and Machine Learning techniques to automatically classify messages as **Spam** or **Not Spam**.

The application preprocesses the input text, converts it into numerical features using **TF-IDF Vectorization**, and predicts the result using a trained Machine Learning model.

---

## ✨ Features

* 📧 Detects whether an email or SMS is Spam or Not Spam.
* ⚡ Fast real-time prediction.
* 📝 Text preprocessing using NLTK.
* 🔍 TF-IDF Vectorization.
* 🤖 Machine Learning based classification.
* 🌐 Interactive Streamlit web application.
* ☁️ Deployed on Streamlit Community Cloud.

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* NLTK
* Pickle

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Text Preprocessing
4. Feature Extraction using TF-IDF
5. Model Training
6. Model Evaluation
7. Model Serialization using Pickle
8. Streamlit Web Application Deployment

---

## 📁 Project Structure

```
Email_spam_detection/
│
├── app.py
├── Email_Spam_Detection.ipynb
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/sachin-418/Email_spam_detection.git
```

### 2. Navigate to the project directory

```bash
cd Email_spam_detection
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

---

## 💡 How to Use

1. Open the Streamlit application.
2. Enter an email or SMS message.
3. Click the **Predict** button.
4. View whether the message is classified as **Spam** or **Not Spam**.

---

## 📈 Future Improvements

* Support for multiple Machine Learning models.
* Probability/confidence score for predictions.
* Email file (.eml) upload support.
* Dark mode UI enhancements.
* Improved text preprocessing and feature engineering.

---

## 📸 Application Preview

You can add screenshots of your application here.

Example:

```
images/
   ├── home.png
   ├── prediction.png
```

---

## 📦 Requirements

```
streamlit
pandas
numpy
scikit-learn
nltk
```

---

## 👨‍💻 Author

**Sachin**

GitHub: https://github.com/sachin-418

---

## ⭐ Support

If you found this project useful:

* ⭐ Star this repository
* 🍴 Fork the repository
* 💬 Share your feedback
* 🛠️ Contribute with improvements

---

## 📄 License

This project is open-source and available under the **MIT License**.
