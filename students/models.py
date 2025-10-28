from django.db import models

# Create your models here.



class ClassRoom(models.Model):
    name = models.CharField(max_length=100)
    grade = models.FloatField()


    def __str__(self):
        return f"{self.name} (Grade{self.grade})"



class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE,related_name="students")
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name