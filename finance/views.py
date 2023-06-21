from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decorators import unauthenticated_user
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Check if username is already taken
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username is already taken.')
            # Check if email is already registered
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'Email is already registered.')

            if not form.errors:
                form.save()
                messages.success(request, 'Account Created Successfully')
                return redirect('login')

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
            messages.error(request, 'Incorrect username or password!')

    return render(request, 'finance/login.html')

@login_required(login_url='login')
def my_profile(request):
   users=User.objects.filter(username=request.user)
   context={'users':users}
   return render(request,'finance/profile.html', context)

@login_required(login_url='login')
def dashboard(request):
    category=Category.objects.all()
    cat_count = category.count()

    income=Income.objects.filter(owner=request.user)
    income_count = income.count()

    budgets = Budget.objects.filter(owner=request.user)
    budget_count = budgets.count()

    debt=Debt.objects.filter(owner=request.user,status='Not Paid')
    debt_count = debt.count()

    expense=Expense.objects.filter(owner=request.user)
    expense_count = expense.count()

    context={'cat_count':cat_count,'budget_count':budget_count,'debt_count':debt_count,'expense_count':expense_count,'income_count':income_count}
    return render(request, 'finance/dashboard.html',context)
    

def index(request):
    return render(request, 'finance/index.html')

def about(request):
    return render(request, 'finance/about.html')

@login_required(login_url='login')
def user_management(request):
    users = User.objects.filter(is_superuser=False)  # Exclude superusers
    return render(request, 'finance/user_management.html',{'users': users})


# delete user
@login_required(login_url='login')
def delete_users(request, id):
    users = get_object_or_404(User, id=id)
    users.delete()
    messages.success(request, 'Users deleted Successfully!')
    return redirect('users')

# delete debt
@login_required(login_url='login')
def delete_debt(request, id):
    debt = get_object_or_404(Debt, id=id)
    debt.delete()
    messages.success(request, 'Debt deleted Successfully!')
    return redirect('debt')

# delete income
@login_required(login_url='login')
def delete_income(request, id):
    income = get_object_or_404(Income, id=id)
    income.delete()
    messages.success(request, 'Income deleted Successfully!')
    return redirect('income')

# delete budget
@login_required(login_url='login')
def delete_budget(request, id):
    bud = get_object_or_404(Budget, id=id)
    bud.delete()
    messages.success(request, 'Budget deleted Successfully!')
    return redirect('budget')

# delete expense
@login_required(login_url='login')
def delete_expenses(request, id):
    exp = get_object_or_404(Expense, id=id)
    exp.delete()
    messages.success(request, 'Expense deleted Successfully!')
    return redirect('expense')

@login_required(login_url='login')
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'finance/category_list.html', {'categories': categories})

@login_required(login_url='login')
def budget_list(request):
    budgets = Budget.objects.filter(owner=request.user).order_by("-created_at")
    budget_count = budgets.count()
    return render(request, 'finance/budget_list.html', {'budgets': budgets,'budget_count':budget_count})

@login_required(login_url='login')
def expense_list(request):
    expenses = Expense.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, 'finance/expense_list.html', {'expenses': expenses})

@login_required(login_url='login')
def income_list(request):
    incomes = Income.objects.filter(owner=request.user).order_by("-created_at")
    total_income = sum(float(inc.amount) for inc in incomes)
    return render(request, 'finance/income_list.html', {'incomes': incomes,'total_income':total_income})


@login_required(login_url='login')
def all_debt(request):
    debts = Debt.objects.filter(owner=request.user).order_by("-created_at")
    total_debts = Debt.objects.filter(owner=request.user,status='Not Paid')
    # Calculate the sum of all debts
    total_debt = sum(float(debt.amount) for debt in total_debts)
    return render(request, 'finance/debt_list.html', {'debts': debts,'total_debt': total_debt})

# create budget
@login_required(login_url='login')
def create_budget(request):
    incomes = Income.objects.filter(owner=request.user)
    total_income = sum(float(inc.amount) for inc in incomes)
    
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            obj=form.save(commit =False)
            obj.owner=request.user
            obj.save()
            messages.success(request, 'Budget created Successfully!')
            return redirect('budget')
    else:
        form = BudgetForm()
    
    return render(request, 'finance/create_budget.html', {'form': form,'total_income':total_income})



# add expense
@login_required(login_url='login')
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
                expense.owner=request.user
                budget_remaining= int(budget_remaining) - int(expense_amount)
                Budget.objects.filter(name=budget_id).update(remaining=budget_remaining)
                expense.save()
                messages.success(request, 'Expense registered Successfully!')
                return redirect('expense')
            else:
                messages.warning(request, 'You dont have enough budget')
                return redirect('add_expense')
    else:
        form = ExpenseForm()
    
    return render(request, 'finance/add_expense.html', {'form': form})



# add category
@login_required(login_url='login')
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

# add income
@login_required(login_url='login')
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            obj=form.save(commit =False)
            obj.owner=request.user
            obj.save()
            messages.success(request, 'Income registered Successfully!')
            return redirect('income')
        else:
            print('error')
    else:
        form = IncomeForm()
    
    return render(request, 'finance/add_income.html', {'form': form})


# add debt
@login_required(login_url='login')
def add_debt(request):
    if request.method == 'POST':
        form = DebtForm(request.POST)
        if form.is_valid():
            obj=form.save(commit =False)
            obj.owner=request.user
            obj.save()
            messages.success(request, 'Debt Added Successfully!')
            return redirect('debt')
    else:
        form = DebtForm()
    
    return render(request, 'finance/add_debt.html', {'form': form})

@login_required(login_url='login')
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

@login_required(login_url='login')
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
