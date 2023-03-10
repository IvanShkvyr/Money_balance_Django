# Generated by Django 4.1.4 on 2023-01-01 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag_costs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag_income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MoneyBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money_movement', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=150)),
                ('money', models.FloatField()),
                ('date_of_entry', models.DateField()),
                ('tags_costs', models.ManyToManyField(to='money_balance.tag_costs')),
                ('tags_income', models.ManyToManyField(to='money_balance.tag_income')),
            ],
        ),
    ]
