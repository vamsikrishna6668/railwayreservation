# Generated by Django 2.1.2 on 2018-10-30 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registrationpage',
            fields=[
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('surname', models.CharField(max_length=10)),
                ('fathername', models.CharField(max_length=10)),
                ('cno', models.IntegerField(default=10, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=10)),
            ],
        ),
    ]
