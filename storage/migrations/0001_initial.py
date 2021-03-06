# Generated by Django 3.2.7 on 2021-10-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('url', models.SlugField(max_length=200)),
                ('date', models.DateTimeField()),
                ('text', models.TextField(blank=True)),
                ('languaje', models.CharField(choices=[('ESP', 'ESP'), ('ENG', 'ENG'), ('OTHER', 'OTHER')], default='OTHER', max_length=6)),
                ('vigilance_category', models.TextField(blank=True)),
                ('information_category', models.TextField(blank=True)),
                ('cita', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
