from django.db import models


class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField()
    toy_category = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150, blank=False)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    class Meta:
        ordering = ('name',)
    def __str__(self):
        return self.name