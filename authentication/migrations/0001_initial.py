# Generated by Django 5.2.3 on 2025-06-19 00:30

import authentication.models
import django.contrib.auth.validators
import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analyst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('registration', models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Registration must have exactly 7 digits and start with the number 5.', regex='^5\\d{6}$')], verbose_name='Registration Number')),
                ('rank', models.CharField(choices=[('SD', 'Soldado'), ('CB', 'Cabo'), ('3 SGT', '3º Sargento'), ('2 SGT', '2º Sargento'), ('1 SGT', '1º Sargento'), ('ST', 'Subtenente'), ('2 TEN', '2º Tenente'), ('1 TEN', '1º Tenente'), ('CAP', 'Capitão'), ('MAJ', 'Major'), ('TC', 'Tenente-Coronel'), ('CEL', 'Coronel')], default='CB', max_length=6, verbose_name='Position in the military hierarchy')),
                ('service_name', models.CharField(max_length=30, verbose_name='Name used in service')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', authentication.models.AnalystManager()),
            ],
        ),
    ]
