# Generated by Django 5.1.4 on 2024-12-23 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=128),
            preserve_default=False,
        ),
    ]
