# Generated by Django 4.2.2 on 2023-06-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_merge_20230627_0917'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='pettable',
        #     name='prompt1',
        # ),
        migrations.AlterField(
            model_name='pettable',
            name='activity_level',
            field=models.CharField(choices=[('Low', 'Less than an hour'), ('Moderate', 'One to two hours'), ('High', 'Two hours minimum')], default='High', max_length=50),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='energy_level',
            field=models.CharField(choices=[('Low', 'Very calm'), ('Moderate', 'Moderate energy level'), ('High', 'High energy')], default='High', max_length=50),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Female', max_length=50),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='healthStatus',
            field=models.CharField(choices=[('Good health', 'Good Health'), ('Needs medication', 'Needs Medication'), ('Disabled', 'Disabled')], default='Disabled', max_length=250),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='monthlyCost',
            field=models.DecimalField(decimal_places=2, default=1.5, max_digits=8),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='size',
            field=models.CharField(choices=[('Small', 'Small, up to 9kg'), ('Medium', 'Medium, up to 27kg'), ('Large', 'Large, up to 45kg'), ('XL', 'Large, over 45kg')], default='Large', max_length=50),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='sociability',
            field=models.CharField(choices=[('Very sociable', 'Very sociable, loves both dogs and people'), ('Somewhat sociable', 'Somewhat sociable, selectively interacts'), ('Hardly sociable', 'Not very sociable, prefers to keep a distance'), ('Not sociable', 'Not sociable, avoids interaction when possible')], default='Not sociable', max_length=40),
        ),
        migrations.AlterField(
            model_name='pettable',
            name='vaccinationInformation',
            field=models.CharField(choices=[('Not vaccinated', 'No'), ('Vaccinated', 'Fully Vaccinated')], default='Not vaccinated', max_length=20),
        ),
    ]
