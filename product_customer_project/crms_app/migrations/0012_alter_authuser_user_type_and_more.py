# Generated by Django 4.0.4 on 2022-05-29 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms_app', '0011_alter_authuser_user_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Customer Manager'), (2, 'Customer'), (4, 'Reviewer'), (1, 'Product Manager')], null=True),
        ),
        migrations.AlterField(
            model_name='customerreview',
            name='reviewDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
