# Generated by Django 4.0.4 on 2022-05-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
