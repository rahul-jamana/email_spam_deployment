import streamlit as st
import pickle
from text_clean import clean_text

# Load trained model (pipeline)
model = pickle.load(open("spam_clf_model.pkl", "rb"))

# Streamlit UI
st.set_page_config(page_title="SMS Spam Detector", layout="centered")

st.title("📩 SMS Spam Detection Dashboard")
st.write("Enter an SMS below and check if it is **Spam** or **Not Spam**.")

# Input box
user_input = st.text_area("✍️ Enter your message here:", "")

# Predict button
if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        cleaned_text = clean_text(user_input)
        prediction = model.predict([cleaned_text])[0]

        if prediction == 1:
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **NOT SPAM**")

