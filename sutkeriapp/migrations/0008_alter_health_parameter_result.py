# Generated by Django 4.1.7 on 2023-03-14 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sutkeriapp', '0007_health_parameter_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='health_parameter',
            name='Result',
            field=models.CharField(max_length=50),
        ),
    ]