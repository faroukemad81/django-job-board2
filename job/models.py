from django.db import models

Job_Type=(
    ('full time', 'full time'),
    ('part time', 'part time'),
)

# Create your models here.
class category(models.Model):
    name= models.CharField(max_length=15)

class Job(models.Model):  #table
    title= models.CharField(max_length=100)  #coloumn
    job_type= models.CharField(max_length=15, choices=Job_Type)
    description= models.TextField(max_length=1000)
    published_at= models.DateTimeField(auto_now=True)
    vacancey= models.IntegerField(default=1)
    salary= models.IntegerField(default=0)
    experience= models.IntegerField(default=2)
    category= models.ForeignKey(category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


