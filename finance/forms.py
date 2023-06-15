
from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'amount', 'category', 'budget','date')
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('name', 'amount', 'start_date', 'end_date')

class DebtForm(forms.ModelForm):
    class Meta:
        model = Debt
        fields = '__all__'
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
        fields = '__all__'
        fields = ('income_no', 'source', 'amount', 'term')
        