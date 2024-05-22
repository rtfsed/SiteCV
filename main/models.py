from django.db import models

class ContactMessage(models.Model):
    name = models.CharField('Name',max_length=100)
    email = models.EmailField('Email')
    message = models.TextField('Message')

    def __str__(self):
        return self.name