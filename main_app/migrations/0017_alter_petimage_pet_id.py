# Generated by Django 4.2.2 on 2023-06-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_remove_pettable_a1_remove_pettable_a2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimage',
            name='pet_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='main_app.pettable'),
        ),
    ]
