# Generated by Django 5.2 on 2025-04-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
