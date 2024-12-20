from django.db import models
from django.urls import reverse

class Grap(models.Model):   #grap is the model name means joke in Dutch
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('grappen:detail', args=[str(self.pk)])

    def __str__(self):
        return self.question
    

    #from grappen.models import Grap ----use it in shell to import the model