from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime
from datetime import datetime, timedelta, date
# Create your models here.


def validate_email(value):
    if not value.endswith('@dawsoncollege.qc.ca'):
        raise ValidationError("Only dawsoncollege emails allowed")


class TheResponsible(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=False)
    email = models.EmailField(validators=[validate_email])


class TheTask(models.Model):
    taskName = models.CharField(max_length=120)
    taskDesc = models.TextField(blank=True)
    start_date = models.DateField(default=datetime.now)
    end_date = models.DateField(default=datetime.now()+timedelta(days=1))
    # end_date = models.DateField(default=set_end_date(start_date))
    owner = models.ForeignKey(TheResponsible, on_delete=models.CASCADE)

