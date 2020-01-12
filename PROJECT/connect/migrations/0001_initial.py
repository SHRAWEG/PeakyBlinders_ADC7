# Generated by Django 3.0.2 on 2020-01-12 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emailid', models.EmailField(max_length=50)),
                ('studentid', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
