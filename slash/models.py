from django.db import models

class SearchResult(models.Model):
    q = models.CharField(max_length=20)
    result = models.CharField(max_length=1000)
    date = models.DateField()
