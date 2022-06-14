from django.db import models

class Sms(models.Model):
    text = models.TextField()
    
    def __str__(self):
        return self.text