# Generated by Django 4.2.2 on 2023-06-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_remove_pettable_prompt1_petmatch_matchstatus'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='pettable',
        #     name='prompt1',
        # ),
        migrations.AddField(
            model_name='userdetails',
            name='liked_pets',
            field=models.ManyToManyField(blank=True, related_name='liked_by', to='main_app.pettable'),
        ),
    ]
