from django.db import models
from django.urls import reverse

class Grap(models.Model):   #grap is the model name means joke in Dutch
    vraag = models.TextField(max_length=200)
    antwoord = models.TextField(max_length=100, blank=True)
    gemaakt = models.DateTimeField(auto_now_add=True)
    geupdate = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('grappen:detail', args=[str(self.pk)])

    def __str__(self):
        return self.vraag
    

    #from grappen.models import Grap ----use it in shell to import the model