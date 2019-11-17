from django.db import models

# Create your models here.
class Quiz(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)

    # def __str__(self):
    #     return self.name

class Questions(models.Model):
    name=models.TextField(blank=True, null=True)
    options=models.TextField(blank=True, null=True)
    correct_option=models.TextField(blank=True, null=True)
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    points=models.IntegerField(default=0)

    # def __str__(self):
    #     return self.name