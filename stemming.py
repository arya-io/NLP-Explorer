import nltk
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download necessary resources
nltk.download('punkt')
nltk.download('stopwords')

def perform_stemming(text, use_snowball=False):
    """
    Function to perform stemming on input text.
    Args:
        text (str): The input text to stem.
        use_snowball (bool): Flag to choose Snowball Stemmer over Porter Stemmer.
    Returns:
        list: List of stemmed words.
    """
    # Initialize the stemmer
    if use_snowball:
        stemmer = SnowballStemmer("english")  # Snowball Stemmer for better performance in some cases
    else:
        stemmer = PorterStemmer()  # Default to Porter Stemmer
    
    # Tokenize the text into words
    word_tokens = word_tokenize(text)
    
    # Remove stopwords and non-alphabetic words (like numbers and special characters)
    stop_words = set(stopwords.words('english'))
    word_tokens = [word for word in word_tokens if word.isalpha() and word.lower() not in stop_words]

    # Perform stemming on each word
    stemmed_words = [stemmer.stem(word) for word in word_tokens]
    
    return stemmed_words

# Test the function
if __name__ == "__main__":
    text = "Running runners are running at a fast speed in the run!"
    result = perform_stemming(text, use_snowball=True)
    print("Stemmed Words:", result)
