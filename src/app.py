import streamlit as st
import joblib
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "spam_pipeline.pkl")
pipeline = joblib.load(model_path)


st.markdown("## *📩 Spam Email Classifier*")

st.write("This app classifies emails or messages as spam or not spam, based on a dataset from Kaggle.")


user_input = st.text_area("Enter the E-mail or text message")



if st.button("Classify"):
    if user_input.strip() == "":
        st.warning("Please enter some text to classify")

    else:
        prediction = pipeline.predict([user_input])[0]
        
        proba = pipeline.predict_proba([user_input])[0]
        confidence = round(proba[prediction]*100,2)

        if prediction==1 and confidence>50:
            st.success(f"Prediction : 🚫 Spam (CONFIDENCE = {confidence}%)")
        elif prediction==0 and confidence>50:
            st.success(f"Prediction : ✅ Not Spam (CONFIDENCE = {confidence}%)")
        else:
            st.warning("Uncertain ⚠️")



