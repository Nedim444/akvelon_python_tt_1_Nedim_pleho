# Generated by Django 3.1.3 on 2021-08-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
