from django.db import models

class Grap(models.Model):   #grap is the model name means joke in Dutch
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
    

    #from grappen.models import Grap ----use it in shell to import the model