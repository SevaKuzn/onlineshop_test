# Generated by Django 4.1.4 on 2023-01-13 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
