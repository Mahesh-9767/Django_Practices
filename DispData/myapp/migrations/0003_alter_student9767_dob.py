# Generated by Django 4.2 on 2025-04-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_student9767_delete_empl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student9767',
            name='dob',
            field=models.DateField(),
        ),
    ]
