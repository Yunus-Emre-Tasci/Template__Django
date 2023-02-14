# Generated by Django 4.1.4 on 2023-02-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number', models.SmallIntegerField()),
                ('image', models.ImageField(blank=True, upload_to='students')),
            ],
        ),
    ]
