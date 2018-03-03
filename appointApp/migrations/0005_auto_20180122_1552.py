# Generated by Django 2.0.1 on 2018-01-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointApp', '0004_auto_20180122_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_doctor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_patient',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_sex',
            field=models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10),
        ),
    ]
