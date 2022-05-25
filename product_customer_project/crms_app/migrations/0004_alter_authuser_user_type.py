# Generated by Django 4.0.4 on 2022-05-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms_app', '0003_alter_authuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Reviewer'), (1, 'Product Manager'), (2, 'Customer'), (3, 'Customer Manager')], null=True),
        ),
    ]