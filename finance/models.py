from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group as AuthGroup
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    role = models.CharField(default='customer')
    user_permissions = models.ManyToManyField(
    'auth.Permission', verbose_name='user permissions',blank=True,related_name='customuser_set',
    help_text='The permissions this user has',related_query_name='user',)
    groups = models.ManyToManyField(
        AuthGroup,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to',
        related_name='customuser_set',
        related_query_name='user',
    )

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    

    def __str__(self):
        return self.name
    
class Debt(models.Model):
    STATUS = (
        ('Not Paid', 'Not Paid'),
        ('Paid', 'Paid'),
    )
    taken_from = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    taken_date=models.DateField()
    status = models.CharField(max_length=200, choices=STATUS, default='Not Paid')
    

    def __str__(self):
        return self.taken_from    

class Budget(models.Model):
    name = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    remaining=models.CharField(max_length=50,default=None)
    start_date = models.DateField()
    end_date = models.DateField()
    def save(self, *args, **kwargs):
        if self.remaining is None:
            self.remaining=self.amount
            super().save(*args, **kwargs)

    # def get_budget_info(self):
    #     return{'name':self.budget.name,'amount':self.budget.amount}

    def __str__(self):
        return self.name

class Expense(models.Model):
    title = models.CharField(max_length=100)
    amount = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE,null='True')
    total_expense=models.CharField(max_length=50,default=None)
    date = models.DateField()

    def save(self, *args, **kwargs):
        if self.total_expense is None:
            self.total_expense=self.amount
            super().save(*args, **kwargs)

    def __str__(self):
        return self.title

