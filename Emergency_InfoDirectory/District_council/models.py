from django.db import models


# Create your models here.
class District_council(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=40, db_column='name')
    chairman = models.CharField(max_length=50, db_column='chairman')
    contact_no = models.CharField(max_length=20, db_column='contact_no')
    district = models.CharField(max_length=30, db_column='district')
    division = models.CharField(max_length=15, db_column='division')

    def __str__(self):
        return self.name+","+self.district+","+self.division
