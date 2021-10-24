from django.db import models
from account.models import *

# Create your models here.
class Year(models.Model):
    year = models.CharField(max_length=4)
    def __str__(self):
        return f'{self.year}'


class Academic_Manpower(models.Model):
    year =  models.ManyToManyField(Year, null=True)
    faculty = models.ManyToManyField(Faculty, null=True)
    master = models.IntegerField(blank=True,default='-', null=True)
    phd = models.IntegerField(blank=True,default='-', null=True)
    exteach = models.IntegerField(blank=True,default='-', null=True)
    teach = models.IntegerField(blank=True,default='-', null=True)
    asst_prof = models.IntegerField(blank=True,default='-', null=True)
    assoc_prof = models.IntegerField(blank=True,default='-', null=True)
    work = models.IntegerField(blank=True,default='-', null=True)
    leave = models.IntegerField(blank=True,default='-', null=True)
    total = models.IntegerField(null=False)
    def __str__(self):
        return f'{self.faculty}'f' {self.year}'

class Service_Manpower(models.Model):
    year =  models.ManyToManyField(Year, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    bhd = models.IntegerField(blank=True,default='-', null=True)
    master = models.IntegerField(blank=True,default='-', null=True)
    sf = models.IntegerField(blank=True,default='-', null=True)
    specific_sf = models.IntegerField(blank=True,default='-', null=True)
    prof = models.IntegerField(blank=True,default='-', null=True)
    specific_prof = models.IntegerField(blank=True,default='-', null=True)
    work = models.IntegerField(blank=True,default='-', null=True)
    leave = models.IntegerField(blank=True,default='-', null=True)
    total = models.IntegerField(null=False)
    def __str__(self):
        return f'{self.position}'f' {self.year}'

class Event(models.Model):
    year =  models.ManyToManyField(Year, null=True)
    faculty = models.ManyToManyField(Faculty, null=True)
    total = models.IntegerField(null=False)
    train_people = models.IntegerField(blank=True,default='-', null=True)
    train_time = models.IntegerField(blank=True,default='-', null=True)
    seminar_people = models.IntegerField(blank=True,default='-', null=True)
    seminar_time = models.IntegerField(blank=True,default='-', null=True)
    observe_people = models.IntegerField(blank=True,default='-', null=True)
    observe_time = models.IntegerField(blank=True,default='-', null=True)
    def __str__(self):
        return f'{self.faculty}'f' {self.year}'

class Budget(models.Model):
    faculty = models.ManyToManyField(Faculty, null=True)
    budgetyear = models.CharField(max_length=4)
    initial_budget = models.IntegerField(blank=True,default='-', null=True)
    total_budget = models.IntegerField(blank=True,default='-', null=True)
    balance = models.IntegerField(blank=True,default='-', null=True)
    def __str__(self):
        return f'{self.faculty}'


class Academice_Outstand(models.Model):
    year =  models.ManyToManyField(Year, null=True)
    rank = models.CharField(max_length=1)
    type_a = models.EmailField(max_length=255, null=True ,default='-')
    name = models.EmailField(max_length=255, null=True,default='-')
    def __str__(self):
        return f'{self.year}'

class Service_Outstand(models.Model):
    year =  models.ManyToManyField(Year, null=True)
    rank = models.CharField(max_length=1)
    type_a = models.EmailField(max_length=255, null=True ,default='-')
    name = models.EmailField(max_length=255, null=True,default='-')
    def __str__(self):
        return f'{self.year}'

class leave_time(models.Model):
    name = models.CharField(max_length=255)
    extend_time = models.IntegerField()
    extend_begin = models.DateField()
    extend_end = models.DateField()
    def __str__(self):
        return f'ครั้งที่ {self.extend_time}' f'{self.name}'

class Study_leave(models.Model):
    degree_choice = (
        ('ปริญญาโท','ปริญญาโท'),
        ('ปริญญาเอก','ปริญญาเอก')
    )
    degree = models.CharField(max_length=10,choices=degree_choice)
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    total_time = models.CharField(max_length=255)
    bursary = models.CharField(max_length=255)
    time = models.ManyToManyField(leave_time, null=True)
    work = models.DateField()
    approval = models.DateField()
    requesting = models.DateField()
    def __str__(self):
        return f'{self.name}' f'ศึกษาต่อ {self.degree}' f'{self.university}' f' ({self.faculty})'



class Pending(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_request = models.DateField()
    date_request_evaluate = models.DateField()
    date_evaluate = models.DateField()
    date_begin = models.DateField()
    date_full_term = models.DateField()
    position_rc = models.CharField(max_length=255)
    situation = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.name}' 

class Document(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    faculty = models.ManyToManyField(Faculty, null=True)
    date_request = models.DateField()
    date_evaluate = models.DateField()
    date_expire = models.DateField()
    level_evaluate_tech = models.CharField(max_length=255)
    level_evaluate_document = models.CharField(max_length=255)
    no_evaluate = models.IntegerField()
    def __str__(self):
        return f'{self.name}' 

class Approval(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status_choice = (
        ('อนุมัติ','อนุมัติ'),
        ('ไม่อนุมัติ','ไม่อนุมัติ')
    )
    status = models.CharField(max_length=10,choices=status_choice)
    position = models.CharField(max_length=255)
    faculty_academic = models.CharField(max_length=255)
    date_request = models.DateField()
    date_approval = models.DateField()
    document = models.TextField()
    publicity = models.TextField()
    def __str__(self):
        return f'{self.name}' 

class Year_plan(models.Model):
    year = models.CharField(max_length=9)
    def __str__(self):
        return f'{self.year}'

class Human_resource(models.Model):
    year = models.ManyToManyField(Year_plan, null=True)
    file = models.FileField(default='default.pdf',upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return f'{self.year}'

class Report(models.Model):
    year = models.ManyToManyField(Year, null=True)
    file = models.FileField(default='default.pdf',upload_to='uploads/%Y/%m/%d/')
    def __str__(self):
        return f'{self.year}'