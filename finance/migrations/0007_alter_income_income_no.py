# Generated by Django 4.2.2 on 2023-06-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0006_alter_income_income_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income_no',
            field=models.IntegerField(unique=True),
        ),
    ]
