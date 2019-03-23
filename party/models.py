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
    parent_state = models.ForeignKey('State', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

