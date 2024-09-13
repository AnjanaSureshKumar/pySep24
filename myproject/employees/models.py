from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'id = {self.id}, name = {self.name}/n'

class Employee(models.Model):
    name = models.CharField(max_length=255)
    dept_id = models.ForeignKey(Department, on_delete= models.CASCADE)
    job_title=models.CharField(max_length=50)
    salary = models.FloatField()
    bonus = models.FloatField()

    def __str__(self):
        return f'id = {self.id}, name = {self.name}, dept_id = {self.dept_id.name}, job_title={self.job_title},salary = {self.salary}, bonus = {self.bonus}'
    