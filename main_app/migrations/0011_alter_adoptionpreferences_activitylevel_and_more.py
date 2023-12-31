# Generated by Django 4.2.2 on 2023-06-23 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_merge_20230623_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoptionpreferences',
            name='activityLevel',
            field=models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], default='low', max_length=50),
        ),
        migrations.AlterField(
            model_name='adoptionpreferences',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], default='small', max_length=1),
        ),
        migrations.AlterField(
            model_name='adoptionpreferences',
            name='sociability',
            field=models.CharField(choices=[('introvert', 'Introvert'), ('extrovert', 'Extrovert'), ('both', 'Both')], default='both', max_length=50),
        ),
    ]
