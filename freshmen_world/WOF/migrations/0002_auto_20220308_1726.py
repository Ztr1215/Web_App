# Generated by Django 2.2.26 on 2022-03-08 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WOF', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=60)),
                ('university', models.CharField(default='', max_length=80)),
                ('degree', models.CharField(default='', max_length=30)),
                ('level', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Student Users',
            },
        ),
        migrations.DeleteModel(
            name='StudentUser',
        ),
    ]
