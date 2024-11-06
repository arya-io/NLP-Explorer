import nltk
import streamlit as st
from tokenization import perform_tokenization
from pos_tagging import perform_pos_tagging
from stemming import perform_stemming
from lemmatization import perform_lemmatization
from ner import perform_ner

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

# Streamlit App Configuration
st.set_page_config(page_title="NLP Explorer", layout="wide")

# Custom CSS to enhance UI and layout
st.markdown(
    """
    <style>
    body {
        background-color: #f4f7fc;
        font-family: 'Roboto', sans-serif;
    }
    .title {
        font-weight: 700;
        font-size: 36px;
        color: #4A6FA2;
        text-align: center;
        margin-bottom: 30px;
    }
    .card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-8px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
    }
    .card h3 {
        color: #5e6e79;
        font-weight: 600;
    }
    .button {
        background-color: #4A90E2;
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .button:hover {
        background-color: #357ABD;
    }
    .feature-checkbox {
        font-size: 16px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #7a8d9c;
        margin-top: 40px;
    }
    .container {
        display: flex;
        justify-content: space-between;
        margin-top: 30px;
    }
    .feature-container {
        flex: 1;
        margin-right: 20px;
    }
    .footer-link {
        color: #4A90E2;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True
)

# App title and description
st.markdown("<h1 class='title'>💬 Natural Language Processing (NLP) Explorer</h1>", unsafe_allow_html=True)
st.markdown("""
Welcome to **NLP Explorer**! Use this app to analyze and process text with the following NLP techniques:
- Tokenization
- Part-of-Speech (POS) Tagging
- Stemming
- Lemmatization
- Named Entity Recognition (NER)

Simply choose the feature you want to apply, input your text, and see the results!
""")

# Text input area with more space
text_input = st.text_area("📝 Enter text for analysis", height=100, placeholder="Type or paste your text here...", max_chars=1000)

# Card layout for NLP features
st.write("### 🛠️ Choose NLP features to apply:")

selected_features = {
    'Tokenization': False,
    'POS Tagging': False,
    'Stemming': False,
    'Lemmatization': False,
    'NER': False
}

# Display features as interactive cards in a 2-column layout
col1, col2 = st.columns(2)

with col1:
    with st.container():
        if st.checkbox("🔍 Tokenization", key="tokenization"):
            selected_features['Tokenization'] = True
            st.markdown("**Tokenization**: Splits text into words or sentences.")
        if st.checkbox("🏷️ POS Tagging", key="pos_tagging"):
            selected_features['POS Tagging'] = True
            st.markdown("**POS Tagging**: Assigns part of speech to each word.")

with col2:
    with st.container():
        if st.checkbox("🌿 Stemming", key="stemming"):
            selected_features['Stemming'] = True
            st.markdown("**Stemming**: Reduces words to their root form.")
        if st.checkbox("📝 Lemmatization", key="lemmatization"):
            selected_features['Lemmatization'] = True
            st.markdown("**Lemmatization**: Converts words to their base form based on context.")
        if st.checkbox("🔍 NER", key="ner"):
            selected_features['NER'] = True
            st.markdown("**NER**: Recognizes named entities in the text.")

# Analyze Text Button with loading and feedback
st.write("---")
if st.button("Analyze Text", key="analyze_button", use_container_width=True):
    if not text_input:
        st.error("⚠️ Please enter some text to analyze.")
    else:
        st.write("### 📊 NLP Analysis Results")

        # Display loading indicator during analysis
        with st.spinner('Analyzing your text...'):
            # Perform Tokenization
            if selected_features['Tokenization']:
                st.markdown("#### 🧩 Tokenization")
                tokenization_result = perform_tokenization(text_input)
                st.write("**Word Tokens:**", tokenization_result['word_tokens'])
                st.write("**Sentence Tokens:**", tokenization_result['sentence_tokens'])

            # Perform POS Tagging
            if selected_features['POS Tagging']:
                st.markdown("#### 🏷️ POS Tagging")
                pos_tagging_result = perform_pos_tagging(text_input)
                st.write("**POS Tags:**", pos_tagging_result)

            # Perform Stemming
            if selected_features['Stemming']:
                st.markdown("#### 🌿 Stemming")
                stemming_result = perform_stemming(text_input)
                st.write("**Stemmed Words:**", stemming_result)

            # Perform Lemmatization
            if selected_features['Lemmatization']:
                st.markdown("#### 📝 Lemmatization")
                lemmatization_result = perform_lemmatization(text_input)
                st.write("**Lemmatized Words:**", lemmatization_result)

            # Perform NER
            if selected_features['NER']:
                st.markdown("#### 🔍 Named Entity Recognition (NER)")
                ner_result = perform_ner(text_input)
                if ner_result:
                    for entity, entity_type in ner_result:
                        st.write(f"**{entity}**: {entity_type}")
                else:
                    st.write("No named entities found.")

# Footer with additional info and social link
st.markdown("---")
st.markdown("""
<div class='footer'>
    💡 NLP Explorer | Built with <a href='https://streamlit.io/' class='footer-link'>Streamlit</a> | Version 1.0.0 | 
    Visit the <a href='https://github.com/arya-io/nlp-explorer' class='footer-link'>GitHub Repo</a>
</div>
""", unsafe_allow_html=True)
