import streamlit as st
import pickle
import string
import nltk
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK data (safe if already installed)
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# -----------------------------
# Text Preprocessing Function
# -----------------------------
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# -----------------------------
# Load Model & Vectorizer
# -----------------------------
tfidf = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("model1.pkl", "rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

st.title("📧 Email Spam Detection")
st.write("Enter an email or SMS message below to check whether it is Spam or Not Spam.")

input_sms = st.text_area("Enter your message")

if st.button("Predict"):

    transformed_sms = transform_text(input_sms)

    vector_input = tfidf.transform([transformed_sms])

    result = model.predict(vector_input)[0]
    
   
    st.markdown(result)
   
