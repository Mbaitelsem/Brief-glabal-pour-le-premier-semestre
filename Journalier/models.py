from django.db import models

class task (models.Model):
    tache = models.CharField(max_length=150)


    def  __str__(self):
        return self.tache

