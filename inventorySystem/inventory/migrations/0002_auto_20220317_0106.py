# Generated by Django 3.0.14 on 2022-03-16 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='last_sale_date',
            new_name='last_sales_date',
        ),
    ]