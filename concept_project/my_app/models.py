from django.db import models

# Create your models here.

class id(models.Model):
    top_name= models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return (self.top_name)


class detail (models.Model):
    name= models.ForeignKey(id,on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)



    def __str__(self):
        return self.location

