from django.db import models


class Cv(models.Model): 
    file = models.FileField(upload_to='cvs/')
    extracted_text = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return self.file.name