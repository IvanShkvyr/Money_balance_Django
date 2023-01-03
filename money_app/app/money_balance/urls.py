from django.urls import path

from . import views

app_name = "money_balance"

urlpatterns = [
    path('', views.main, name='main'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_costs/', views.add_costs, name='add_costs'),
    path('add_category_costs/', views.add_category_costs, name='add_category_costs'),
    path('add_category_income/', views.add_category_income, name='add_category_income'),
    path('report/', views.report, name='report'),
    path('report_sum', views.report, name='report_sum' )
]
