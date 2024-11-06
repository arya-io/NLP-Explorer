import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag

# Download necessary resources
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')

# Mapping POS tags to WordNet POS tags
def get_wordnet_pos(treebank_tag):
    """
    Convert treebank POS tags to WordNet POS tags
    Args:
        treebank_tag (str): The POS tag in Treebank format.
    Returns:
        str: Corresponding WordNet POS tag.
    """
    if treebank_tag.startswith('V'):
        return 'v'  # verb
    elif treebank_tag.startswith('N'):
        return 'n'  # noun
    elif treebank_tag.startswith('R'):
        return 'r'  # adverb
    else:
        return 'n'  # default to noun if unknown

def preprocess_text(text):
    """
    Preprocess the input text by cleaning it and removing unnecessary elements like URLs and emails.
    Args:
        text (str): The raw input text.
    Returns:
        str: Cleaned text ready for NLP processing.
    """
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    # Remove special characters and digits
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def perform_lemmatization(text):
    """
    Function to perform lemmatization on input text.
    Args:
        text (str): The input text to lemmatize.
    Returns:
        list: List of lemmatized words.
    """
    # Preprocess the text before applying lemmatization
    cleaned_text = preprocess_text(text)

    # Tokenize the text into words
    word_tokens = word_tokenize(cleaned_text)
    
    # Get POS tags for each token
    pos_tags = pos_tag(word_tokens)
    
    lemmatizer = WordNetLemmatizer()
    
    # Lemmatize words with correct POS tag
    lemmatized_words = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags
    ]
    
    return lemmatized_words

# Test the function
if __name__ == "__main__":
    text = "The children are playing in the garden. The cats were running fast."
    result = perform_lemmatization(text)
    print("Lemmatized Words:", result)
