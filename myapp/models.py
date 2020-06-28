from django.db import models

# Create your models here. cafe1
class building(models.Model):
    b_name=models.CharField(max_length=200)
    b_floor=models.CharField(max_length=200)
    b_distance=models.CharField(max_length=200)
    b_location=models.CharField(max_length=200)
    def __str__(self):
        return self.b_name
class menuinfo(models.Model):
    build= models.ForeignKey(building, on_delete=models.CASCADE)
    m_name=models.CharField(max_length=200)
    m_price=models.CharField(max_length=200)
    m_info=models.CharField(max_length=200)
    def __str__(self):
        return self.m_name

class detailaboutcafe(models.Model):
    cafe=models.ForeignKey(building,on_delete=models.CASCADE)
    d_openhour=models.CharField(max_length=200)
    d_characteristic=models.CharField(max_length=200)
    d_seats=models.CharField(max_length=200)
    def __str__(self):
        return self.d_characteristic

