import streamlit as st
import os
import openai
from secKey import openapi_key

# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key
openai.api_key = openapi_key

# List of supported languages
languages = [
    "English",
    "Hindi",
    "French",
    "Telugu",
    "Albanian",
    "Bengali",
    "Bhojpuri",
    "Brazilian Portuguese",
    "Chinese",
    "Dutch",
    "Georgian",
    "German",
    "Greek",
    "Gujarati",
    "Haryanvi",
    "Hungarian",
    "Indonesian",
    "Irish",
    "Italian",
    "Japanese",
    "Kannada",
    "Korean",
    "Maithili",
    "Mandarin Chinese",
    "Marathi",
    "Marwari",
    "Nepali",
    "Norwegian",
    "Oriya",
    "Portuguese",
    "Punjabi",
    "Romanian",
    "Russian",
    "Sanskrit",
    "Serbian",
    "Ukrainian",
    "Urdu"
]

# Function to translate text using GPT-3.5 Turbo
def translate_text(text, source_language, target_language):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text."},
            {"role": "user", "content": f"Translate the following text from {source_language} to {target_language}:\n{text}"}
        ],
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    # Extract translation from the response
    translation = response['choices'][0]['message']['content'].strip()
    return translation

# Streamlit web app
def main():
    st.title("Translate My Text")

    # Input text
    text = st.text_area("Enter the text to translate")

    # Source language dropdown
    source_language = st.selectbox("Select source language", languages)

    # Target language dropdown
    target_language = st.selectbox("Select target language", languages)

    # Translate button
    if st.button("Translate"):
        if not text.strip():
            st.warning("Please enter some text to translate.")
        elif source_language == target_language:
            st.warning("Source and target languages must be different.")
        else:
            translation = translate_text(text, source_language, target_language)
            st.markdown(
                f'<p style="color: blue; font-size: 25px;">{translation}</p>',
                unsafe_allow_html=True
            )

if __name__ == '__main__':
    main()
