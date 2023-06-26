# Generated by Django 4.2.2 on 2023-06-26 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0029_remove_petmatch_matchstatus_remove_pettable_prompt1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pettable',
            name='prompt1',
        ),
        migrations.AlterField(
            model_name='pettable',
            name='user',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
