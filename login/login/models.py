# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return "{0} {1} {2}".format(self.first_name, self.middle_name, self.last_name)

    
class Parent(Person):
    parent_id = models.IntegerField(primary_key=True)

##default parent
##default=Parent(first_name='Default', middle_name='', last_name='Parent', dob='09/23/1988', address='124 bery grey', parent_id=0)

class Child(Person):

    parent_of_child = models.ForeignKey(Parent, on_delete=models.CASCADE, null=True)
    school = models.CharField(max_length=20)


class School(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    school_types = (('Elementary', 'Elementary School'), ('Middle','Middle School'), ('High', 'High School'), ('Vocational', 'Vocational School'),)
    school_type = models.CharField(max_length=20, choices=school_types, default='Elementary')



