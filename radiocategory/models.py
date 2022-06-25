#from django.db import models
from __future__ import unicode_literals
from django.db import models
from model_utils import Choices
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Radcategory(models.Model):
    radusr = models.ForeignKey(User, on_delete=models.CASCADE, related_name='radusr')
    # NICK NAME should be unique
    nick_name = models.CharField(verbose_name='Institution Name', max_length=100, unique =  True)
    name = models.CharField(verbose_name='Technology name',blank=True, null=True, max_length=100)
    HARDWARE = Choices('True', 'False')
    hardware = models.CharField(choices=HARDWARE, blank=True, null=True, max_length=100)
    SOFTWARE = Choices('True', 'False')
    software = models.CharField(choices=SOFTWARE, blank=True, null=True, max_length=100)
    LICENSED = Choices('True', 'False')
    licensed = models.CharField(choices=LICENSED, blank=True, null=True, max_length = 250)
    BOTH = Choices('True', 'False')
    both = models.CharField(choices=BOTH, blank=True, null=True, max_length = 250)
    OPEN_SOUCE = Choices('True', 'False')
    open_souce = models.CharField(choices=OPEN_SOUCE, blank=True, null=True, max_length = 250)
    DEVELOPED = Choices('True', 'False')
    developed = models.CharField(choices=OPEN_SOUCE, blank=True, null=True, max_length = 250)
    capacity = models.CharField(blank=True, null=True, max_length = 250)
    STATUS = Choices('In use', 'Abandoned', 'Defective')
    status = models.CharField(choices=STATUS, blank=True, null=True, max_length = 250)
#    dob = models.DateField(auto_now=False, auto_now_add=False)
#    lives_in = models.CharField(max_length=150, null = True, blank = True)
 

    def __str__(self):
        return self.name + self.hardware