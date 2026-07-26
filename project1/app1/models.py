from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class chef(models.Model):
    name=models.CharField(max_length=100)
    specialization=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
        return self.name

class category(models.Model):
    name=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class menuitem(models.Model):
    name=models.CharField(max_length=150)
    category=models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    chef=models.ForeignKey(chef, on_delete=models.SET_NULL, null=True)
    price=models.DecimalField(max_digits=6, decimal_places=2,validators=[MinValueValidator(0.01)])
    description=models.TextField(blank=True,null=True)
    is_available=models.BooleanField(default=True)

class dinning_table(models.Model):
    table_number=models.IntegerField(unique=True)
    capacity=models.IntegerField(default=2)
from django import forms
class add_menuitem(forms.ModelForm):
    class Meta:
        model=menuitem
        fields=['name','category','chef','price','description','is_available']

class new_chef(forms.ModelForm):
    class Meta:
        model=chef
        fields=['name','specialization']