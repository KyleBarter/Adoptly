# Generated by Django 4.2.2 on 2023-06-26 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0024_delete_redirectmodel_remove_pettable_prompt1_and_more'),
    ]

    operations = [
        # migrations.RemoveField(
        #     model_name='pettable',
        #     name='prompt1',
        # ),
        migrations.AlterField(
            model_name='userdetails',
            name='adopter',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
