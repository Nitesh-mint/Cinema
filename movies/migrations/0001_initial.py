# Generated by Django 4.2.4 on 2023-09-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('length', models.CharField(max_length=100)),
                ('trailer_link', models.CharField(max_length=300)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]
