# Generated by Django 2.2.3 on 2019-07-18 14:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^a-zA-Z]*$', 'Only alphabets are allowed.')]),
        ),
    ]
