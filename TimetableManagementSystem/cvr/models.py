from django.db import models

# Create your models here.

class Subject(models.Model):
    name=models.CharField(max_length=200,primary_key=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    rollNo=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200)
    subject=models.CharField(max_length=200)

    def __str__(self):
        return self.rollNo

class Branch(models.Model):
    branch_name=models.CharField(max_length=20,default='None')
    sections=models.IntegerField(default=0)
    subjects=models.CharField(max_length=200,default='None')
    year=models.IntegerField(default=0)

    def __str__(self):
        return str(self.branch_name)+" "+str(self.year)

    class Meta:
        unique_together = (('branch_name' ,'year'),)

class TimeTable(models.Model):
    branch_name=models.ForeignKey(Branch,on_delete=models.CASCADE)
    section=models.CharField(max_length=1)
    year=models.IntegerField()
    monday=models.CharField(max_length=200)
    tuesday = models.CharField(max_length=200)
    wednesday = models.CharField(max_length=200)
    thursday = models.CharField(max_length=200)
    friday = models.CharField(max_length=200)
    saturday = models.CharField(max_length=200)

    class Meta:
        unique_together = (('branch_name', 'section','year'),)

    def __str__(self):
        return str(self.branch_name)+" "+str(self.section)

class Student(models.Model):
    rollno=models.CharField(max_length=200,primary_key=True)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    section=models.CharField(max_length=1)

    def __str__(self):
        return self.rollno

class Admin(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=50)

