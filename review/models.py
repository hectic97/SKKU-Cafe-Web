from django.db import models
from myapp.models import building

# Create your models here.
class evaluation(models.Model):
    build=models.ForeignKey(building,on_delete=models.CASCADE)
    e_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)

class facilityreview(models.Model):
    f_build = models.ForeignKey(building, on_delete=models.CASCADE)
    f_text = models.CharField(max_length=200)
    f_votes = models.IntegerField(default=0)
class moodreview(models.Model):
    m_build = models.ForeignKey(building, on_delete=models.CASCADE)
    m_text = models.CharField(max_length=200)
    m_votes = models.IntegerField(default=0)
