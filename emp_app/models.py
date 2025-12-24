from django.db import models

# Create your models here.
class emp_model(models.Model):
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    email=models.EmailField()
    loc=models.CharField(max_length=40)

    def __str__(self):
        return self.name

