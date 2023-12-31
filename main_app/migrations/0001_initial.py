

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('phone', models.IntegerField()),
                ('adopter', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PetTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('sociability', models.CharField(choices=[('introvert', 'Introvert'), ('extrovert', 'Extrovert'), ('both', 'Both')], max_length=40)),
                ('age', models.IntegerField()),
                ('breed', models.TextField(max_length=100)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('weight', models.FloatField()),
                ('healthStatus', models.CharField(choices=[('good health', 'Good Health'), ('needs medication', 'Needs Medication'), ('disabled', 'Disabled')], max_length=250)),
                ('activity_level', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], max_length=50)),
                ('vaccinationInformation', models.CharField(choices=[('N', 'No'), ('Y', 'Fully Vaccinated')], max_length=1)),
                ('monthlyCost', models.DecimalField(decimal_places=2, max_digits=8)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetMatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchStatus', models.CharField(max_length=50)),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pettable')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.pettable')),
            ],
        ),
        migrations.CreateModel(
            name='AdoptionPreferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activityLevel', models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], max_length=50)),
                ('sociability', models.CharField(choices=[('introvert', 'Introvert'), ('extrovert', 'Extrovert'), ('both', 'Both')], max_length=50)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
