# 📩 Spam Email Classifier

A simple NLP-based Streamlit web app that classifies email or text messages as **Spam** or **Not Spam**, using a Logistic Regression model trained on a dataset from Kaggle.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-streamlit-cloud-link)  
*(Update this after deploying)*

---

## 🧠 What It Does

- Takes a text/email input from the user
- Uses a trained **TF-IDF + Logistic Regression** model to predict
- Displays:
  - ✅ Not Spam / 🚫 Spam
  - Confidence Score (e.g., 83.45%)
  - ⚠️ "Uncertain" if prediction confidence is low

---

## 🛠️ Tech Stack

- **Python**
- **Scikit-learn** – for ML model and TF-IDF vectorizer
- **Streamlit** – to build the web interface
- **Joblib** – to save/load the model pipeline

---

## 📊 Model Details

- **Model**: Logistic Regression  
- **Vectorizer**: TfidfVectorizer  
- **Training Data**: [Kaggle SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  
- **Accuracy**: ~97% on test data  
- **Confidence Threshold**: >50% = confident, otherwise "Uncertain"

---

## 📂 Project Structure

