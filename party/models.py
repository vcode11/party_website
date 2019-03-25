from django.db import models

# Create your models here.
class State(models.Model):
    """
        Model for states in India.
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class District(models.Model):
    """
        Model for districts in various states.
    """
    name = models.CharField(max_length=200)
    parent_state = models.ForeignKey('State', on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name

class Member(models.Model):
    """
        Model to store data of members of  party
    """
    name = models.CharField(max_length=200),
    dob  = models.DateField(blank=True,null=True),
    gender = models.CharField(max_length=1,default='M'),
    email = models.EmailField(blank=True),
    phone = models.CharField(max_length=10),
    state = models.CharField(max_length=50),
    district = models.CharField(max_length=50,),
    address = models.CharField(max_length=200,blank=True),
    pincode = models.CharField(max_length=6,blank=True),
    voterID = models.CharField(max_length=10,blank=True),




