import nltk
import re

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')

def perform_tokenization(text):
    """
    Function to perform both word and sentence tokenization
    Args:
        text (str): input text to be tokenized
    Returns:
        dict: word tokens and sentence tokens
    """
    # Preprocessing: Clean the text to remove excessive whitespace, handle special characters, etc.
    text = text.strip()  # Remove leading and trailing whitespace
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    
    # Sentence Tokenization
    sentence_tokens = nltk.sent_tokenize(text)
    
    # Word Tokenization with more precise handling (retaining special characters correctly)
    word_tokens = nltk.word_tokenize(text)
    
    # Advanced Tokenization: Customize tokenizing for certain patterns (e.g., dates, numbers, etc.)
    word_tokens = [token for token in word_tokens if token not in nltk.corpus.stopwords.words('english')]  # Remove stopwords
    
    return {
        'word_tokens': word_tokens,
        'sentence_tokens': sentence_tokens
    }

# Test the function
if __name__ == "__main__":
    text = "This is a test. I have a sentence like: '2024-11-07' or URLs like https://example.com!"
    result = perform_tokenization(text)
    print("Word Tokens:", result['word_tokens'])
    print("Sentence Tokens:", result['sentence_tokens'])
