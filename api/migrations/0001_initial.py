# Generated by Django 5.1.2 on 2024-10-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('telegram_id', models.CharField(max_length=50, unique=True)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('lang', models.CharField(max_length=2)),
            ],
        ),
    ]
