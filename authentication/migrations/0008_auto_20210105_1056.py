# Generated by Django 3.1.4 on 2021-01-05 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20210105_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useralert',
            name='alert_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='useralert',
            name='alert_email_body',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='useralert',
            name='alert_email_subject',
            field=models.CharField(max_length=100),
        ),
    ]
