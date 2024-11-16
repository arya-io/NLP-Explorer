import nltk
import re
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def perform_pos_tagging(text):
    """
    Function to perform POS tagging with preprocessing to improve accuracy.
    Args:
        text (str): input text for POS tagging
    Returns:
        list: list of tuples with word and its POS tag
    """
    # Step 1: Preprocessing
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    
    # Remove URLs, emails, and other unwanted entities
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # Remove URLs
    text = re.sub(r'\S+@\S+', '', text)  # Remove email addresses
    
    # Step 2: Tokenize text
    tokens = nltk.word_tokenize(text)
    
    # Step 3: Remove stopwords (commonly ignored in many NLP tasks)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.lower() not in stop_words]
    
    # Step 4: POS tagging using NLTK's built-in tagger
    pos_tags = nltk.pos_tag(tokens)
    
    return pos_tags

# Test the function
# if __name__ == "__main__":
#     text = "The quick brown fox jumps over the lazy dog. Check out this link: https://example.com!"
#     result = perform_pos_tagging(text)
#     print("POS Tags:", result)
