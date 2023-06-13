from django.urls import path
# from finance.views import category_list, budget_list, expense_list,index,add_expense,create_category, register,signin
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/', views.category_list, name='category'),
    path('budgets/', views.budget_list, name='budget'),
    path('expenses/add', views.add_expense, name='add_expense'),
    path('budget/create', views.create_budget, name='create-budget'),
    path('expenses/', views.expense_list, name='expense'),
    path('category/create', views.create_category, name='create_category'),
    path('register/', views.register, name='register'),
    path('login/', views.signin, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('category/delete/<int:id>', views.delete_category, name='delete-category'),
    path('expenses/delete/<int:id>', views.delete_expenses, name='delete-expenses'),
    path('budget/delete/<int:id>', views.delete_budget, name='delete-budget'),
    path('debt/add', views.add_debt, name='add_debt'),
    path('debt/', views.all_debt, name='debt'),
    path('expenses/update/<int:id>', views.edit_debt_status, name='edit_debt_status'),
    path('users/', views.user_management, name='users'),
    path('users/delete/<int:id>', views.delete_users, name='delete-users'),
    path('about', views.about, name='about'),
]