from django.db import models

# Create your models here.
class Employee(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    DOJ = models.CharField(max_length=100)
    email= models.CharField(max_length=100)



class LeaveManagement(models.Model):
    empid=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=100)
    leavedate=models.CharField(max_length=100)
    reason=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    leavebucket=models.CharField(max_length=100)
    hr_approval=models.CharField(max_length=100,default='FALSE')
    TL_approval= models.CharField(max_length=100,default='FALSE')


class Profile(models.Model):
    empid = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    DOJ = models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    avl_leaves= models.CharField(max_length=100)



