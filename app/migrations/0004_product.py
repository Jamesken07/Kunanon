# Generated by Django 4.2 on 2024-03-15 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_store_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_id', models.IntegerField(unique=True)),
                ('Product_location', models.CharField(max_length=100)),
            ],
        ),
    ]
