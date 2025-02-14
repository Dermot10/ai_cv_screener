import pdfplumber
import time
import json
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import action
from .models import Cv
from .serializers import CvSerializer
from .utils import preprocess_text, extract_skills, extract_education, extract_experience, calculate_similarity


class CvUploadView(ViewSet): 
    parser_classes = (MultiPartParser, FormParser)

    @action(detail=False, methods=['post'])
    def cv_experience_check(Self, request, *args, **kwargs): 
        file = request.FILES.get('file')
        cv = Cv.objects.create(file=file)

        if not file:
            return Response({'error': 'No file uploaded'}, status=400)

        if file.name.endswith('pdf'): 
            with pdfplumber.open(cv.file.path) as pdf:
                cv.extracted_text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])

                cleaned_text = preprocess_text(cv.extracted_text)
                extracted_skills = extract_skills(cleaned_text)
                extracted_education = extract_education(cleaned_text)
                extracted_experience = extract_experience(cleaned_text)
                time.sleep(1)
                cv.save()

        return Response({
            'message':'CV uploaded', 
            #'text':cv.extracted_text,
            'extracted skills': extracted_skills,
            'extracted experience': extracted_experience,
            'extracted education': extracted_education,
        })

    @action(detail=False, methods=['post'])
    def compare_similarity(self, request, *args, **kwargs): 
        file = request.FILES.get('file')
        cv = Cv.objects.create(file=file)
        job_posting = request.POST.get("job_posting", "").strip()

        if not file:
            return Response({"error": "Missing file"}, status=400)

        if not job_posting:
            return Response({"error": "Missing job description"}, status=400)

        if file.name.endswith('pdf') or file.name.endswith('docx'): 
            with pdfplumber.open(cv.file.path) as f:
                cv.extracted_text = '\n'.join([page.extract_text() for page in f.pages if page.extract_text()])
                cleaned_text = preprocess_text(cv.extracted_text)
                cleaned_job_advert = preprocess_text(job_posting)
                similarity_score = calculate_similarity(cleaned_text, cleaned_job_advert)
                time.sleep(2)
                cv.save()
        return Response(
            {
            'message':'CV uploaded',
            'Resume Match Score' : f'{similarity_score:.2f}'}
            )

