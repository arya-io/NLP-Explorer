# NLP Explorer

## 🧑‍💻 Overview

**NLP Explorer** is a web-based application built with **Streamlit** that allows users to explore various **Natural Language Processing (NLP)** techniques. It provides an intuitive interface to perform multiple NLP tasks, including:

- **Tokenization**: Splits text into individual words or sentences.
- **POS Tagging**: Assigns part-of-speech labels to words in a sentence.
- **Stemming**: Reduces words to their root form.
- **Lemmatization**: Converts words to their base form using contextual analysis.
- **Named Entity Recognition (NER)**: Identifies and categorizes named entities in the text.

The application aims to provide a hands-on experience with NLP and can be used to better understand the key concepts in text processing and analysis.

## 🚀 Features

- **Interactive Web Interface**: Built using **Streamlit** for easy interaction and text processing.
- **Multiple NLP Tasks**: Users can choose from Tokenization, POS Tagging, Stemming, Lemmatization, and NER.
- **Real-time Results**: See the results of each NLP technique immediately after applying it to your text.
- **Preprocessing**: Text is preprocessed before analysis to remove irrelevant characters like URLs, emails, etc.

## 📌 Installation

### 1. Clone the repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/nlp-explorer.git
```

### 2. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

requirements.txt includes the necessary dependencies such as:
- `streamlit`
- `nltk`

### 3. Download NLTK Data

The project uses the nltk library, which requires additional data downloads. You can download the necessary datasets by running:

```bash
python -c "import nltk; nltk.download('punkt'); nltk.download('wordnet'); nltk.download('omw-1.4'); nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_ne_chunker'); nltk.download('words'); nltk.download('stopwords')"
```

## 🚀 Usage

### 1. Run the Streamlit app

After installing the dependencies and downloading the NLTK data, you can start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

This will open a new tab in your default web browser with the NLP Explorer interface.

### 2. Using the App

- **Input Text:** Type or paste any text into the text input box.
- **Choose NLP Tasks:** Check the boxes for the NLP tasks you want to apply (Tokenization, POS Tagging, Stemming, Lemmatization, NER).
- **Analyze:** Click the "Analyze Text" button to see the results of the selected NLP techniques.
- **View Results:** Results for each NLP task will be displayed below the input text area.

## 🧑‍🤝‍🧑 Contributing

We welcome contributions to the NLP Explorer project! Here’s how you can help:

Fork the repository and clone it to your local machine.
Create a new branch for your changes.
Make your changes to the code.
Commit your changes with clear messages.
Push your changes to your forked repository.
Create a pull request to the main repository.
Please make sure your code follows Python’s PEP 8 style guidelines and includes comments where necessary. Additionally, add tests for any new functionality.

## 🛠️ Built With

- **Streamlit:** Framework for building interactive web apps.
- **NLTK:** Natural Language Toolkit for performing various NLP tasks.
- **Python:** Programming language used for the development of the app.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
