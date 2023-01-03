from datetime import date, datetime

from django.shortcuts import render, redirect
from django.db.models import OuterRef, Subquery, Sum

from .forms import CategoryCostsForm, CategoryIncomeForm, IncomeForm, CostsForm, ReportForm
from .models import Tag_income, Tag_costs, MoneyBalance

# Create your views here.
def main(request):
    return render(request, 'money_balance/index.html', {})


def add_income(request):
    tags = Tag_income.objects.all()
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            note = form.save()
            choice_tags = Tag_income.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags:
                note.tags_income.add(tag)
            return redirect(to="money_balance:main")
        else:
            return render(request, 'money_balance/add_income.html',  context={'form': form, 'tags': tags})
    return render(request, 'money_balance/add_income.html', context={'form': IncomeForm(), 'tags': tags})


def add_costs(request):
    tags = Tag_costs.objects.all()
    if request.method == 'POST':
        form = CostsForm(request.POST)
        if form.is_valid():
            note = form.save()
            choice_tags = Tag_costs.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags:
                note.tags_costs.add(tag)
            return redirect(to="money_balance:main")
        else:
            return render(request, 'money_balance/add_costs.html',  context={'form': form, 'tags': tags})
    return render(request, 'money_balance/add_costs.html', context={'form': CostsForm(), 'tags': tags})


def add_category_costs(request):
    if request.method == 'POST':
        form = CategoryCostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="money_balance:main")
        else:
            return render(request, 'money_balance/add_category_costs.html', context={'form': form})
    return render(request, 'money_balance/add_category_costs.html', context={'form': CategoryCostsForm()})


def add_category_income(request):
    if request.method == 'POST':
        form = CategoryIncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="money_balance:main")
        else:
            return render(request, 'money_balance/add_category_income.html', context={'form': form})
    return render(request, 'money_balance/add_category_income.html', context={'form': CategoryIncomeForm()})


def report(request):
    list_of_receipts = MoneyBalance.objects.all()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():

            date_from = datetime.strptime(form['date_from'].value(), '%Y-%m-%d').date()
            date_to = datetime.strptime(form['date_to'].value(), '%Y-%m-%d').date()

            list_of_receipts_all = list_of_receipts.filter(
                date_of_entry__range=[date_from, date_to]
            )
            total_money = list_of_receipts_all.aggregate(total=Sum('money'))

            list_of_receipts_costs = list_of_receipts.filter(
                money_movement__icontains='Costs',
                date_of_entry__range=[date_from, date_to]
            )
            total_costs = list_of_receipts_costs.aggregate(total=Sum('money'))

            list_of_receipts_income = list_of_receipts.filter(
                money_movement__icontains='Income',
                date_of_entry__range=[date_from, date_to]
            )
            total_income = list_of_receipts_income.aggregate(total=Sum('money'))

            return render(request, 'money_balance/report_sum.html', context={
                'date_from':date_from,
                'date_to':date_to,
                'total_income': total_income,
                'total_costs': total_costs,
                'total_money': total_money
                })
        else:
            return render(request, 'money_balance/report.html', context={'form': form})

    return render(request, 'money_balance/report.html', context={'form': ReportForm()})
