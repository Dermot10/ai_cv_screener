from contextlib import contextmanager
import pdfplumber
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt_tab')
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return ' '.join(words)

def extract_skills(text): 
    skills = ['python', 'django', 'flask', 'fastapi', 'sql', 'machine learning', 'aws', 'docker',
    'REST API', 'graphQL', 'websockets', 'PostgreSQL', 'MySQL', 'NoSQL', 'kubernetes', 'CI/CD',
    'jenkins', 'AWS', 'Azure', 'GCP', 'Lambda', 'S3', 'EC2', 'Git', 'GitHub', 'Bitbucket', 'GitLab',
    'Linux', 'Bash', 'Shell scripting', 'Microservices', 'Event-driven architecture', 'RabbitMQ', 'Kafka', 
    'OOP', 'Design Patterns', 'SOLID', 'Security', 'Authentication', 'OAuth', 'JWT', 
    'Testing', 'Unit tests', 'PyTest', 'Selenium', 'Playwright' 'Agile', 'Scrum', 'Kanban', 'Scikit-learn', 'Splunk',
    'Numpy', 'Pandas', 'SIEM', 'cyber', ''  ]
    extracted_skills = [skill.lower() for skill in skills if skill in text]
    return extracted_skills


def extract_experience(text): 
    experience = ['developer', 'software', 'automation', 'backend', 'engineer', 'engineering', 'systems',
    'Developed', 'Designed', 'Implemented', 'Maintained', 'Scalable', 'Optimized', 'High-performance', 
    'Secure', 'Integrated', 'Deployed', 'Automated', 'Tested','Led', 'Managed', 'Collaborated', 'Worked with',
    'Agile', 'Scrum', 'Stand-ups', 'Sprints', 'Cloud-based', 'On-premise', 'Hybrid', 'Debugged', 'Troubleshot',
    'Refactored', 'API development', 'Database management', 'Performance tuning', 'Worked on', 'Contributed to', 
    'Participated in', 'Architected', 'Built', 'Designed from scratch']
    experience = [exp.lower() for exp in experience if exp in text]
    return experience

def extract_education(text):
    education = ['science', 'math', 'maths', 'stem', 'cs', 'engineering', 'economics',
    'Bachelor’s', 'Master’s', 'PhD', 'Software Engineering', 'Information Technology', 'University', 
    'College', 'Institution', 'Bootcamp', 'Certification', 'Online Course', 'Degree', 'Diploma', 
    'Certification', 'Coursework', 'Thesis', 'Research']
    education = [subject.lower() for subject in education if subject in text]
    return education 

def calculate_similarity(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]  # Return similarity score


def open_pdf(file_path):
    """Context manager to open and extract text from a PDF file using pdfplumber."""
    try:
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            yield text  # Pass the extracted text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        yield None 

