
from django.urls import path
from . import views

app_name = 'budget_app'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('transactions/', views.transactions, name = 'transactions'),
    path('transaction/<int:transaction_id>/', views.transaction, name='transaction'),
    path('new_entry/<int:transaction_id>/', views.new_entry , name='new_entry'),
    path('bar_chart/', views.bar_chart, name='bar_chart'),
    path('delete/<int:entry_id>/',views.delete, name='delete'),

]