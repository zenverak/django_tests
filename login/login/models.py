# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    

    def __str__(self):
        return "{0} {1} {2}".format(self.first_name, self.middle_name, self.last_name)

    
class Parent(Person):
    parent_id = models.IntegerField(primary_key=True)

##default parent
##default=Parent(first_name='Default', middle_name='', last_name='Parent', dob='09/23/1988', address='124 bery grey', parent_id=0)

class Child(Person):
    grades = (('PreK','Preschool'),
              ('KG', 'Kindergarten'),
              ('1st','First Grade'),
              ('2nd','Second Grade'),
              ('3rd', 'Third Grade'),
              ('4th', 'Fourth Grade'),
              ('5th', 'Fifth Grade'),
              ('6th', 'Sixth Grade'),
              ('7th', 'Seventh Grade'),
              ('8th', 'Eigth Grade'),
              ('9th', 'Ninth Grade'),
              ('10th', 'Tenth Grade'),
              ('11th', 'Eleventh Grade'),
              ('12th', 'Twelth Grade'),
              )

    parent_of_child = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=20 )
    grade = models.CharField(max_length=20, choices=grades, null=True)


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    school_types = (('Elementary', 'Elementary School'), ('Middle','Middle School'), ('High', 'High School'), ('Vocational', 'Vocational School'),)
    school_type = models.CharField(max_length=20, choices=school_types, default='Elementary')

class RandIds(models.Model):
    id_number = models.CharField(max_length=15, primary_key=True)
    



