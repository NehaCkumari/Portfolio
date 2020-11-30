from django.db import models

# Create your models here.
class contact(models.Model):
    Name = models.CharField("name", max_length=255, blank = True, null = True)
    email = models.EmailField()
    subject = models.CharField("subject", max_length=255, blank = True, null = True)
    describe = models.CharField("message", max_length=255, blank = True, null = True)
    



