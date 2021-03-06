# Generated by Django 3.1.5 on 2021-01-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('extension_name', models.CharField(blank=True, max_length=10, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('parent_contact', models.CharField(max_length=11, verbose_name='parent contact number')),
                ('parent_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
