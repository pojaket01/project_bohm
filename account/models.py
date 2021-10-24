from functools import total_ordering
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.http import request

# Create your models here.

class Faculty(models.Model):
    faculty = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.faculty

class User(AbstractUser):
    image = models.ImageField(default='default.jpg',upload_to='profile_pics', null=True)
    id_Position = models.CharField(max_length=20, null=True)
    title_choice = (
        ('นาย','นาย'),
        ('นาง','นาง'),
        ('นางสาว','นางสาว'),
    )
    title_name = models.CharField(max_length=10, blank=True, null=True, choices=title_choice)
    name_en = models.CharField(max_length=100, null=True)
    personal_choice = (
        ('พนักงานมหาวิทยาลัย','พนักงานมหาวิทยาลัย'),
        ('ลูกจ้างชั่วคราว','ลูกจ้างชั่วคราว')
    )
    personal_type = models.CharField(max_length=255, blank=True, null=True, choices=personal_choice)
    line_of_work_choice = (
        ('วิชาการ','วิชาการ'),
        ('สนับสนุน','สนับสนุน')
    )
    line_of_work = models.CharField(max_length=100, blank=True, null=True, choices=line_of_work_choice)
    position_choice = (
        ('อาจารย์','อาจารย์'),
        ('เจ้าหน้าที่บริหารงานทั้วไป','เจ้าหน้าที่บริหารงานทั้วไป'),
        ('บุคลากร','บุคลากร'),
        ('นักวิชาการศึกษา','นักวิชาการศึกษา'),
        ('นักวิเคราะห์นโยบายและเเผน','นักวิเคราะห์นโยบายและเเผน'),
        ('นักประชาสัมพันธ์','นักประชาสัมพันธ์'),
        ('นักวิทยาศาสตร์','นักวิทยาศาสตร์'),
        ('นักวิชาการโสตทัศนศึกษา','นักวิชาการโสตทัศนศึกษา'),
        ('นักวิชาการคอมพิวเตอร์','นักวิชาการคอมพิวเตอร์'),
        ('ครู','ครู')
    )
    position = models.CharField(max_length=100, blank=True, null=True, choices=position_choice)
    academic_choice = (
        ('ศาสตราจารย์','ศาสตราจารย์'),
        ('รองศาสตราจารย์','รองศาสตราจารย์'),
        ('ผู้ช่วยศาสตราจารย์','ผู้ช่วยศาสตราจารย์'),
        ('เชี่ยวชาญ','เชี่ยวชาญ'),
        ('ชำนาญการพิเศษ','ชำนาญการพิเศษ'),
        ('ชำนาญการ','ชำนาญการ')
    )
    academic_position = models.CharField(max_length=100, blank=True, null=True, choices=academic_choice)
    director_choice = (
        ('คณบดี','คณบดี'),
        ('รองคณบดี','รองคณบดี'),
        ('ผู้ช่วยคณบดี','ผู้ช่วยคณบดี'),
        ('ประธานหลักสูตร','ประธานหลักสูตร'),
        ('หัวหน้างาน','หัวหน้างาน')
    )
    director_position = models.CharField(max_length=100, blank=True, null=True, choices=director_choice)
    start_work_date = models.DateField(blank=True , default=None, null=True)
    placement_date = models.DateField(blank=True , default=None, null=True)
    status_job = models.DateField(blank=True , default=None, null=True)
    date_birth = models.DateField(blank=True , default=None, null=True)
    nationality = models.CharField(max_length=100, null=True)

    religion_choice = (
        ('พุทธ','พุทธ'),
        ('คริสต์','คริสต์'),
        ('อิสลาม','อิสลาม'),
        ('ยิว','ยิว'),
        ('ซิกข์','ซิกข์'),
        ('บาไฮ','บาไฮ'),
        ('โซโรอัสเตอร์','โซโรอัสเตอร์'),
        ('พราหมณ์-ฮินดู','พราหมณ์-ฮินดู'),
        ('เชน','เชน'),
        ('ไม่มีศาสนา','ไม่มีศาสนา')
    )
    religion_con = models.CharField(max_length=100, blank=True, null=True, choices=religion_choice)

    phone = models.CharField(max_length=10, null=True)
    email_UP = models.EmailField(max_length=255, null=True)
    address = models.TextField(null=True)
    faculty_id = models.ManyToManyField(Faculty, null=True)

    
    
    degree = models.CharField(max_length=100, null=True)
    faculty = models.CharField(max_length=100, null=True)
    university = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length=40, null=True)
    country = models.CharField(max_length=40, null=True)
    study_date = models.DateField(blank=True , default=None, null=True)
    graduate = models.DateField(blank=True , default=None, null=True)
    gpa = models.FloatField(null=True)
    honors = models.CharField(max_length=100, null=True)
    use_choice = (
        ('ใช้','ใช้'),
        ('ไม่ใช้','ไม่ใช้')
    )
    use_choice_con = models.CharField(max_length=9, blank=True, null=True, choices=use_choice)
    def __str__(self):
        return f'{self.faculty}' f' {self.degree}'

    degree_Master = models.CharField(max_length=100, null=True)
    faculty_Master = models.CharField(max_length=100, null=True)
    university_Master = models.CharField(max_length=100, null=True)
    province_Master = models.CharField(max_length=40, null=True)
    country_Master = models.CharField(max_length=40, null=True)
    study_date_Master = models.DateField(blank=True , default=None, null=True)
    graduate_Master = models.DateField(blank=True , default=None, null=True)
    gpa_Master = models.FloatField(null=True)
    honors_Master = models.CharField(max_length=100, null=True)
    use_choice_Master = (
        ('ใช้','ใช้'),
        ('ไม่ใช้','ไม่ใช้')
    )
    use_choice_con_Master = models.CharField(max_length=9, blank=True, null=True, choices=use_choice_Master)
    def __str__(self):
        return f'{self.faculty}' f' {self.degree_Master}'

    
    degree_doctorate = models.CharField(max_length=100, null=True)
    faculty_doctorate = models.CharField(max_length=100, null=True)
    university_doctorate = models.CharField(max_length=100, null=True)
    province_doctorate = models.CharField(max_length=40, null=True)
    country_doctorate = models.CharField(max_length=40, null=True)
    study_date_doctorate = models.DateField(blank=True , default=None, null=True)
    graduate_doctorate = models.DateField(blank=True , default=None, null=True)
    gpa_doctorate = models.FloatField(null=True)
    honors_doctorate = models.CharField(max_length=100, null=True)
    use_choice_doctorate = (
        ('ใช้','ใช้'),
        ('ไม่ใช้','ไม่ใช้')
    )
    use_choice_con_doctorate = models.CharField(max_length=9, blank=True, null=True, choices=use_choice_doctorate)
    def __str__(self):
        return f'{self.faculty}' f' {self.degree_doctorate}'

#------------------------------------Profile----------------------------------------------------------------------------#