from django.db import models

class register(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    clas=models.IntegerField()
    school=models.CharField(max_length=100)

    def __str__(self):
        return self.name 
class dele(models.Model):
    name=models.CharField(max_length=10)
    def __str__(self):
        return self.name
class search(models.Model):
    
    name=models.CharField(max_length=10)

