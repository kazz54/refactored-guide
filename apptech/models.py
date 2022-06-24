from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from model_utils import Choices
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
User = get_user_model()


    


class TechRev(models.Model):
    eth = models.ForeignKey(User, on_delete=models.CASCADE, related_name='eth')    
    CATEGORY_OF_TECHNOLOGIES = Choices('Laboratory', 'Radiology', 'Microbiology', 'Others')
    category_of_technologies = models.CharField(choices=CATEGORY_OF_TECHNOLOGIES, blank=True, null=True, max_length=30)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
   
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.ethical_considerations)
        