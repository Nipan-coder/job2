# Generated by Django 3.2.5 on 2021-07-14 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jtitle', models.CharField(max_length=70)),
                ('cname', models.CharField(max_length=70)),
                ('eto', models.FloatField()),
                ('efrom', models.FloatField()),
                ('sto', models.FloatField()),
                ('sfrom', models.FloatField()),
                ('location', models.CharField(max_length=70)),
                ('dec', models.TextField()),
            ],
        ),
    ]
