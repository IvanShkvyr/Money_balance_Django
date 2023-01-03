from django.forms import Form, ModelForm, CharField, TextInput, FloatField, NumberInput, DateField, DateInput
from . import models


class CategoryCostsForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput(attrs={"class": "test_class"}))

    class Meta:
        model = models.Tag_costs
        fields = ['name']


class CategoryIncomeForm(ModelForm):
    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput(attrs={"class": "test_class"}))

    class Meta:
        model = models.Tag_income
        fields = ['name']


class IncomeForm(ModelForm):
    money_movement = CharField(required=True, empty_value='Income')
    description = CharField(min_length=3, max_length=150, required=True, widget=TextInput(attrs={"class": "test_class"}))
    money = FloatField(min_value=0, required=True, widget=NumberInput())
    date_of_entry = DateField(widget=DateInput())

    class Meta:
        model = models.MoneyBalance
        fields = ['money_movement', 'description', 'money', 'date_of_entry']
        exclude = ['tags_costs', 'tags_income']


class CostsForm(ModelForm):
    money_movement = CharField(required=True, empty_value='Costs')
    description = CharField(min_length=3, max_length=150, required=True, widget=TextInput(attrs={"class": "test_class"}))
    money = FloatField(max_value=0, required=True, widget=NumberInput())
    date_of_entry = DateField(widget=DateInput())

    class Meta:
        model = models.MoneyBalance
        fields = ['money_movement', 'description', 'money', 'date_of_entry']
        exclude = ['tags_costs', 'tags_income']


class ReportForm(Form):
    date_from = DateField(widget=DateInput())
    date_to = DateField(widget=DateInput())
