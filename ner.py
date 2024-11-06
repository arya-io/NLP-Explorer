import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
import re
from nltk.corpus import stopwords

# Download necessary resources
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

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
    # Remove special characters and digits (optional: depends on task)
    text = re.sub(r'[^A-Za-z\s]', '', text)
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def perform_ner(text):
    """
    Function to perform Named Entity Recognition (NER) on input text.
    Args:
        text (str): The input text to recognize named entities.
    Returns:
        list: List of named entities recognized in the text.
    """
    # Preprocess the text before applying NER
    cleaned_text = preprocess_text(text)
    
    # Tokenize the cleaned text
    tokens = word_tokenize(cleaned_text)
    
    # Perform POS tagging
    pos_tags = pos_tag(tokens)
    
    # Perform Named Entity Recognition (NER)
    named_entities = ne_chunk(pos_tags)
    
    # Extract named entities
    entities = []
    for chunk in named_entities:
        if isinstance(chunk, Tree):  # If the chunk is a named entity
            entity = " ".join([token for token, pos in chunk.leaves()])
            entity_type = chunk.label()  # The type of the named entity (e.g., PERSON, ORGANIZATION)
            entities.append((entity, entity_type))
    
    return entities

# Test the function
if __name__ == "__main__":
    text = "Barack Obama was born on August 4, 1961, in Honolulu, Hawaii. Visit us at https://example.com for more info."
    result = perform_ner(text)
    print("Named Entities:", result)
