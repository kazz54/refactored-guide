# Generated by Django 3.0.10 on 2022-06-24 12:07

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
            name='Radcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=100, unique=True, verbose_name='Institution Name')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Technology name')),
                ('hardware', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100, null=True)),
                ('software', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=100, null=True)),
                ('licensed', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=250, null=True)),
                ('both', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=250, null=True)),
                ('open_souce', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=250, null=True)),
                ('developed', models.CharField(blank=True, choices=[('True', 'True'), ('False', 'False')], max_length=250, null=True)),
                ('capacity', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, choices=[('In use', 'In use'), ('Abandoned', 'Abandoned'), ('Defective', 'Defective')], max_length=250, null=True)),
                ('radusr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='radusr', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
