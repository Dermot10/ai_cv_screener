import pytest
from unittest.mock import patch, MagicMock
from .utils import (
    preprocess_text, extract_skills, extract_experience, 
    extract_education, calculate_similarity, open_pdf
)


sample_text = "Experienced Python developer with expertise in Django, Flask, and AWS."
sample_job_ad = "We are looking for a Python developer skilled in Django and AWS."

def test_preprocess_text():
    text = "Hello, this is a TEST! 123"
    expected = "hello test"
    assert preprocess_text(text) == expected

def test_extract_skills():
    text = preprocess_text(sample_text)
    expected_skills = ['python', 'django', 'flask', 'aws']
    assert set(filter(None, extract_skills(text))) == set(expected_skills)

def test_extract_experience():
    text = preprocess_text("Developed scalable backend systems and automated deployments.")
    expected_experience = ['developed', 'scalable', 'automated']
    assert set(filter(None, extract_experience(text))) == set(expected_experience)


def test_extract_education():
    text = preprocess_text("He studied Computer Science at a University.")
    expected_education = ['science', 'university']
    assert set(filter(None, extract_education(text))) == set(expected_education)

def test_calculate_similarity():
    similarity_score = calculate_similarity(sample_text, sample_job_ad)
    assert 0 <= similarity_score <= 1  # Similarity should be a valid percentage


if __name__ == "__main__":
    pytest.main()