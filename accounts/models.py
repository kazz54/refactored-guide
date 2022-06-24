from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .managers import CustomUserManager
from model_utils import Choices
from django_countries.fields import CountryField



class User(AbstractBaseUser, PermissionsMixin):
    institution_name = models.CharField(max_length=50)
    name = models.CharField(verbose_name='Your Name', max_length=30)
#    SEX = Choices('male', 'female')
#    sex = models.CharField(choices=SEX, default=SEX.male, max_length=20)
    TITLE = Choices('Mr', 'Mrs', 'Miss', 'Ms', 'Dr', 'Prof')
    title = models.CharField(verbose_name='Your Title', choices=TITLE, default=TITLE.Mr, max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    institution_address = models.CharField(max_length=30)
    section = models.CharField(verbose_name='Section/Unit/Derpartment', max_length=30)
    region = models.CharField(blank=True, null=True, max_length=50)
    #    research_specific_objectives = models.CharField(blank=True, null=True, max_length=300)
    SECTOR_YOUR_INSTITUTION_BELONG = Choices('HLI', 'R&D', 'Company', 'Regulatory', 'Others')
    sector_your_instution_belongs = models.CharField(verbose_name='To which sector does your institution belong (e.g. HLI or R&D or Company)',choices=SECTOR_YOUR_INSTITUTION_BELONG, blank=True, null=True, max_length=30)
    other_institution_belong = models.CharField(blank=True, null=True, max_length=500)
    CATEGORY_OF_INSTITUTION = Choices('Public', 'Private')
    category_of_institution = models.CharField(verbose_name='To which of the categories does your institution fall?', choices=CATEGORY_OF_INSTITUTION, blank=True, null=True, max_length=50)
    MANDATE_OF_INSTITUTION = Choices('Treatment/Prevention', 'Research', 'Manufacturing', 'Others')
    mandate_of_institution = models.CharField(verbose_name='What is the mandate of your institution', choices=MANDATE_OF_INSTITUTION, blank=True, null=True, max_length=50)
    other_mandate_of_institution = models.CharField(blank=True, null=True, max_length=500)
#   Technologies			
#    location_typedd = models.CharField(blank=True, null=True, max_length=500)
#    CATEGORY_OF_TECHNOLOGIES = Choices('Laboratory', 'Radiology', 'Microbiology', 'Others (specify)')
#    Category_of_technologies = models.CharField(verbose_name='Which categories of technologies does your institution use?',choices=CATEGORY_OF_TECHNOLOGIES, blank=True, null=True, max_length=60)
#    other_category_of_tech = models.CharField(blank=True, null=True, max_length=500)
#   Technologies available from Laboratory category										    
    
#    date_of_birth = models.DateTimeField(blank=True, null=True)
#    passportimg = models.ImageField(verbose_name='Passport image', default='default.jpg', blank=True, null=True, upload_to='photos/%Y/%m/%d/')
#    ROLE = Choices('Yes', 'No')
#    role = models.CharField(choices=ROLE, verbose_name='Are you Tanzanian?', default=False, max_length=20)
    is_mvp = models.BooleanField(default=False)
    is_svp = models.BooleanField(default=False)
    is_spo = models.BooleanField(default=False)
    is_rev = models.BooleanField(default=False)
    is_drcp = models.BooleanField(default=False)
    is_mgt = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['institution_name', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return self.institution_name