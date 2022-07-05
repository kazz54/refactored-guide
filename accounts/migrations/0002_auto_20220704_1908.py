# Generated by Django 3.2.13 on 2022-07-04 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='quetion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_mvp',
            field=models.BooleanField(default=False, verbose_name='Are you resposible for adding equipment to the database?'),
        ),
    ]
