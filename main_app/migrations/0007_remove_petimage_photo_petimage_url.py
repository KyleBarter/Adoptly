# Generated by Django 4.2.2 on 2023-06-22 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_pettable_prompt1_alter_pettable_prompt2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petimage',
            name='photo',
        ),
        migrations.AddField(
            model_name='petimage',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
