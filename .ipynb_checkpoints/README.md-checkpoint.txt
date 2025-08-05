# 📨 Spam Classifier using Logistic Regression

This project is a **binary text classifier** that distinguishes between **spam** and **ham** (non-spam) SMS messages using **TF-IDF vectorization** and **Logistic Regression**.

Built entirely in **Google Colab** and trained on the classic `spam.csv` dataset, this is a beginner-friendly machine learning project to understand natural language processing workflows.

---

## 🔧 Features

- Preprocessing and cleaning of raw SMS text
- Manual train-test split using pandas
- TF-IDF vectorization using `TfidfVectorizer`
- Model training with `LogisticRegression`
- Performance evaluation using:
  - Accuracy
  - Precision, Recall, F1-Score
  - Confusion Matrix (visualized with matplotlib)

---

## 📁 Files

- `spam_classifier.ipynb`: Main Colab notebook containing the full project
- `spam.csv`: Dataset (must be uploaded manually each session when running in Colab)

---

## 🚀 How to Run This Notebook

> ⚠️ Since Google Colab sessions reset, you must upload `spam.csv` **manually** each time you run the notebook.

### Step-by-step:

1. Open the notebook in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR-USERNAME/spam-classifier/blob/main/spam_classifier.ipynb)

2. Upload the `spam.csv` file in the first code cell:
```python
from google.colab import files
uploaded = files.upload()
