# Generated by Django 4.1.7 on 2023-03-04 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='work_time',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
    ]