# Generated by Django 3.1.4 on 2020-12-31 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAlert',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('sms_mobile_number', models.PositiveIntegerField(null=True)),
                ('sms_body', models.CharField(blank=True, max_length=100, null=True)),
                ('alert_email', models.CharField(blank=True, max_length=100, null=True)),
                ('alert_email_subject', models.CharField(blank=True, max_length=100, null=True)),
                ('alert_email_body', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
