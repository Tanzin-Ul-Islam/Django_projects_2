# Generated by Django 3.0.7 on 2020-06-24 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_follow'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='full_name',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
