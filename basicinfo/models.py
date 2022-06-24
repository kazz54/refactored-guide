from django.conf import settings
from django.db import models
from django.utils import timezone
from datetime import datetime
from model_utils import Choices
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model
User = get_user_model()




class Assesment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
#    research_title = models.CharField(blank=True, null=True, max_length=300)
#    research_introduction = models.CharField(blank=True, null=True, max_length=500)
#    research_broad_objectives = models.CharField(blank=True, null=True, max_length=300)
#    research_specific_objectives = models.CharField(blank=True, null=True, max_length=300)
    SECTOR_YOUR_INSTITUTION_BELONG = Choices('HLI', 'R&D', 'Company', 'Regulatory', 'Others')
    sector_your_instution_belongs = models.CharField(verbose_name='To which sector does your institution belong (e.g. HLI or R&D or Company)',choices=SECTOR_YOUR_INSTITUTION_BELONG, blank=True, null=True, max_length=30)
    CATEGORY_OF_INSTITUTION = Choices('Public', 'Private')
    category_of_institution = models.CharField(verbose_name='To which of the categories does your institution fall?', choices=CATEGORY_OF_INSTITUTION, blank=True, null=True, max_length=50)
    MANDATE_OF_INSTITUTION = Choices('Treatment/Prevention', 'Research', 'Manufacturing', 'Others (specify)')
    mandate_of_institution = models.CharField(verbose_name='What is the mandate of your institution', choices=MANDATE_OF_INSTITUTION, blank=True, null=True, max_length=50)
#   Technologies			
#    location_typedd = models.CharField(blank=True, null=True, max_length=500)
    CATEGORY_OF_TECHNOLOGIES = Choices('Laboratory', 'Radiology', 'Microbiology', 'Others (specify)')
    Category_of_technologies = models.CharField(verbose_name='Which categories of technologies does your institution use?',choices=CATEGORY_OF_TECHNOLOGIES, blank=True, null=True, max_length=60)
#   Technologies available from Laboratory category										    
    
    submitted = models.BooleanField(default=False, blank=True, null=True)
    STATUS = Choices('Saved', 'Internal screaning', 'Rejected', 'Accept')
    status = models.CharField(choices=STATUS, default='Saved', null=True, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(auto_now=True, editable=True, null=True)
    is_spo = models.BooleanField(default=False, blank=True, null=True)
    STATUS_SPO = Choices('Assign to reviwer', 'Return', 'Rejected',)
    status_spo = models.CharField(choices=STATUS_SPO, null=True, max_length=200)
    is_rev = models.BooleanField(verbose_name='reviwer', default=False, blank=True, null=True)
    STATUS_REV = Choices('Assign to DRCP', 'Return', 'Rejected',)
    status_rev = models.CharField(choices=STATUS_REV, blank=True, null=True, max_length=200)
    is_drcp = models.BooleanField(default=False, blank=True, null=True)
    STATUS_DRCP = Choices('Assign to Menagment', 'Return', 'Rejected',)
    status_drcp = models.CharField(choices=STATUS_DRCP, blank=True, null=True, max_length=200)
    is_mgt = models.BooleanField(default=False, blank=True, null=True)
    STATUS_MGT = Choices('Accept', 'Return', 'Rejected', 'POSTPONE',)
    status_mgt = models.CharField(choices=STATUS_MGT, blank=True, null=True, max_length=200)
#    pending = models.BooleanField(default=True)
#    is_active = models.BooleanField(default=True)
#    modified.    
    
#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

    def __str__(self):
        return str(self.sector_your_instution_belongs)