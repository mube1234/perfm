# Generated by Django 4.2.2 on 2023-06-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='total_expense',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='budget',
            name='remaining',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
