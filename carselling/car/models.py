from django.db import models
from django.contrib.auth.models import User
import datetime
from dateutil.relativedelta import relativedelta
from django.core.validators import RegexValidator
# Create your models here.



def to_tuple(lst):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


def get_years(current_year):
    #looping last 20 years
    year_list = [[str(current_year.year),str(current_year.year)]]
    for d in range(20):
        current_year -= relativedelta(years=1)
        year_list.append([str(current_year.year),str(current_year.year)])
    return year_list

def to_tuple(lst):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
class Car(models.Model):

    CONDITION_CHOICES = [
        ('poor','Poor'),
        ('fair','Fair'),
        ('good','Good'),
        ('excellent','Excellent')
    ]
    year_lists = to_tuple(get_years(datetime.datetime.now()))
    name = models.CharField(max_length = 255, null = False, blank = False)
    mobile = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True)
    make = models.CharField(max_length = 255, null = False, blank = False)
    model = models.CharField(max_length = 255, null = False, blank = False)
    year = models.CharField(max_length = 255, choices=year_lists,null = False, blank = False)
    condition = models.CharField(max_length = 255, choices=CONDITION_CHOICES,  null = False, blank = False)
    price = IntegerRangeField(min_value=1000, max_value=100000, null = False, blank = False)
    sold = models.BooleanField(default=False)
    created_on = models.DateTimeField(default = datetime.datetime.now)

class BuyCar(models.Model):
    name = models.CharField(max_length = 255, null = False, blank = False)
    mobile = models.CharField(validators = [phoneNumberRegex], max_length = 16,null=False,blank=False)
    car = models.ForeignKey(Car, on_delete = models.CASCADE, null = True, blank = True)
    created_on = models.DateTimeField(default = datetime.datetime.now)



