
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

# class RegistrationForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ExpenseForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Expense
        fields = ('title', 'amount', 'category', 'budget','date')
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BudgetForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Budget
        fields = ('name', 'amount', 'start_date', 'end_date')
       

class DebtForm(forms.ModelForm):
    taken_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Debt
        fields = ('taken_from', 'amount', 'taken_date')
        widgets = {

           'status': forms.TextInput(attrs={'type': 'hidden'}),
        }
# form for updating debt status
class DebtEditForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = ['status']
        widgets = {
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }
class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        exclude = ('owner','total_income')
        widgets = {
            'identity': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
        