from django.db import models

# Create your models here.


class Staffs_profile(models.Model):
    name = models.CharField(max_length=50, null= False, blank = False)
    mobile = models.CharField(max_length=11, null= False, blank = False)
    levels = models.ManyToManyField('Level')
    qualifications = models.ManyToManyField('Qualification')
    experience = models.CharField(max_length=500, null= False, blank = False)
    marital_status = models.ManyToManyField('Relationship')




    def __str__(self):
        return self.name


class Level(models.Model):
    rank = models.CharField(max_length= 30, null= False, blank = False)

    def __str__(self):
        return self.rank
    
class Qualification(models.Model):
    education = models.CharField(max_length=50, null= False, blank = False)

    def __str__(self):
        return self.education
    

class Relationship(models.Model):
    status = models.CharField(max_length=20, null= False, blank = False)

    def __str__(self):
        return self.status


