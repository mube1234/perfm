from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as AuthGroup
from django.db import models
from django.contrib.auth.models import User
import uuid

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Income(models.Model):
    terms = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='1') 
    identity = models.UUIDField(default=uuid.uuid4, unique=True)
    source = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    total_income=models.CharField(max_length=50,default=None)
    term = models.CharField(max_length=200, choices=terms, default='Monthly')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.total_income is None:
            self.total_income=self.amount
            super().save(*args, **kwargs)

    def __str__(self):
        return self.total_income 

class Budget(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    remaining=models.CharField(max_length=50,default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.remaining is None:
            self.remaining=self.amount
            super().save(*args, **kwargs)

    # def get_budget_info(self):
    #     return{'name':self.budget.name,'amount':self.budget.amount}

    def __str__(self):
        return self.name

class Debt(models.Model):
    STATUS = (
        ('Not Paid', 'Not Paid'),
        ('Paid', 'Paid'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    taken_from = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    taken_date=models.DateField()
    status = models.CharField(max_length=200, choices=STATUS, default='Not Paid')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.taken_from    



class Expense(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE,null='True')
    total_expense=models.CharField(max_length=50,default=None)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def save(self, *args, **kwargs):
        if self.total_expense is None:
            self.total_expense=self.amount
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

