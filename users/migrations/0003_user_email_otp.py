# Generated by Django 4.2.2 on 2023-06-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
