from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from django.shortcuts import render, redirect, get_object_or_404

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'finance/registration.html', {'form': form})

@unauthenticated_user
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page or home page
            return redirect('index')
        else:
            # Invalid credentials, show error message
            messages.info(request, 'Incorrect username or password!')

    return render(request, 'finance/login.html')


def index(request):
    return render(request, 'finance/index.html')

def about(request):
    return render(request, 'finance/about.html')

def user_management(request):
    users = CustomUser.objects.all()
    return render(request, 'finance/user_management.html',{'users': users})

# delete user
def delete_users(request, id):
    users = get_object_or_404(CustomUser, id=id)
    users.delete()
    messages.success(request, 'Users deleted Successfully!')
    return redirect('users')

def dashboard(request):
    return render(request, 'finance/dashboard.html')


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finance/category_list.html', {'categories': categories})

def budget_list(request):
    budgets = Budget.objects.all()
    return render(request, 'finance/budget_list.html', {'budgets': budgets})

def expense_list(request):
    expenses = Expense.objects.all()
    return render(request, 'finance/expense_list.html', {'expenses': expenses})

def all_debt(request):
    debts = Debt.objects.all()
    total_debts = Debt.objects.filter(status='Not Paid')
    # Calculate the sum of all debts
    total_debt = sum(float(debt.amount) for debt in total_debts)
    return render(request, 'finance/debt_list.html', {'debts': debts,'total_debt': total_debt})

# create budget
def create_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Budget created Successfully!')
            return redirect('budget')
    else:
        form = BudgetForm()
    
    return render(request, 'finance/create_budget.html', {'form': form})

# delete budget
def delete_budget(request, id):
    bud = get_object_or_404(Budget, id=id)
    bud.delete()
    messages.success(request, 'Budget deleted Successfully!')
    return redirect('budget')

# add expense
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense_amount = form.cleaned_data['amount'] #current expense
            # ama = form.cleaned_data['amount']
            budget_id = form.cleaned_data['budget']
            budget_remaining=Budget.objects.filter(name=budget_id).values('remaining').first()['remaining']
            
           
            if budget_remaining > expense_amount:
                expense=form.save(commit=False)
                # total_expense=Expense.objects.get(amount=ama).total_expense
                # total_expenses= int(expense_amount) + int(total_expense)
                # Expense.objects.filter(budget=budget_id).update(total_expense=total_expenses)
                
                budget_remaining= int(budget_remaining) - int(expense_amount)
                Budget.objects.filter(name=budget_id).update(remaining=budget_remaining)
                expense.save()
                messages.success(request, 'Expense registered Successfully!')
                return redirect('expense')
            else:
                print('eorror')
                messages.warning(request, 'You dont have enough budget')
                return redirect('add_expense')
    else:
        form = ExpenseForm()
    
    return render(request, 'finance/add_expense.html', {'form': form})

# delete expense
def delete_expenses(request, id):
    exp = get_object_or_404(Expense, id=id)
    exp.delete()
    messages.success(request, 'Expense deleted Successfully!')
    return redirect('expense')

# add category
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added Successfully!')
            return redirect('category')
    else:
        form = CategoryForm()
    
    return render(request, 'finance/create_category.html', {'form': form})

# add debt
def add_debt(request):
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Debt Added Successfully!')
            return redirect('debt')
    else:
        form = DebtForm()
    
    return render(request, 'finance/add_debt.html', {'form': form})


def edit_debt_status(request, id):
    debt = get_object_or_404(Debt, id=id)
    if request.method == 'POST':
        form = DebtEditForm(request.POST, instance=debt)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.status = "Paid"
            obj.save()
            messages.success(request, 'Debt Paid Successfully!')
            return redirect('debt')

    else:
        form = DebtEditForm(instance=debt)

    context = {'form': form,'debt':debt}
    return render(request, 'finance/update_debt_status.html', context)




def user_logout(request):
    logout(request)
    return redirect('index')

def delete_category(request, id):
    cat = get_object_or_404(Category, id=id)
    cat.delete()
    messages.success(request, 'Category deleted Successfully!')
    return redirect('category')

# def edit_category(request, category_id):
#     category = Category.objects.get(id=category_id)
#     if request.method == 'POST':
#         form = CategoryForm(request.POST, instance=category)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')
#     else:
#         form = CategoryForm(instance=category)
    
#     return render(request, 'edit_category.html', {'form': form})
