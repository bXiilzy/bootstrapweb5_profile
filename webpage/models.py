from django.db import models

# Create your models here.
RREFIX_CHOICES = [
    ('นาย', 'นาย'),  
    ('นาง', 'นาง'),
    ('นางสาว', 'นางสาว'),
]

class Students(models.Model):
    stid = models.CharField(unique=True)
    name_prefix = models.CharField(choices=RREFIX_CHOICES, max_length=10)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    
    def __str__(self):
        return str(self.stid)


class Subjects(models.Model):
    subject_code = models.CharField(max_length=20, verbose_name="รหัสวิชา")
    subject_name = models.CharField(max_length=100, verbose_name="ชื่อวิชา")
    teacher_name = models.CharField(max_length=100, verbose_name="ชื่อผู้สอน")

    def __str__(self):
        return str(self.subject_code)