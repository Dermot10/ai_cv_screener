import pdfplumber
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Cv
from .serializers import CvSerializer


class CvUploadView(ViewSet): 
    parser_classes = (MultiPartParser, FormParser)

    def create(Self, request, *args, **kwargs): 
        file = request.FILES['file']
        cv = Cv.objects.create(file=file)

        if file.name.endswith('pdf'): 
            with pdfplumber.open(cv.file.path) as pdf:
                cv.extracted_text = '\n'.join([page.extract_text() for page in pdf.pages if page.extract_text()])
                cv.save()
        return Response({'message':'CV uploaded', 'text':cv.extracted_text})