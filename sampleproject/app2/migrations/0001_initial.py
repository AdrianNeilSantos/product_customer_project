# Generated by Django 4.0.4 on 2022-05-07 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0002_model2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, default='Male', max_length=10, null=True)),
                ('model1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.model1')),
            ],
        ),
    ]