import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text )
    words = [word for word in words if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ''.join(words)


def extract_skills(text): 
    skills = ['python', 'django', 'flask', 'fastapi', 'sql', 'machine learning', 'aws', 'docker']
    extracted_skills = [skill for skill in skills if skill in text]
    return extracted_skills


def extract_experience(text): 
    pass 

def extract_education(text):
    pass


if __name__=="__main__": 
    test_text = 'Experienced Python developer with expertise in Django, Flask, and AWS.'
    print(f"skills found in cv: {extract_skills(preprocess_text(test_text))}")