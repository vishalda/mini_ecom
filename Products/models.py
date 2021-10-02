from django.db import models

# Create your models here.
class Products(models.Model):
    image=models.ImageField(upload_to="images")
    title=models.CharField(max_length=50)
    description=models.TextField()
    price=models.CharField(max_length=20)
    def __str__(self):
        return self.title