from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    sub = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='service_images/',default=" ")

    def __str__(self):
        return self.name

class Faq(models.Model):
    
    name = models.CharField(max_length=100)
    # sub= models.CharField(max_length=100)
    desc = models.TextField()

    def __str__(self):
        return self.name

        