import nltk

def download_nltk_resources():
    try:
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        nltk.download('stopwords')
        print("NLTK resources successfully downloaded.")
    except Exception as e:
        print(f"Error downloading NLTK resources: {e}")

if __name__ == "__main__":
    download_nltk_resources()
