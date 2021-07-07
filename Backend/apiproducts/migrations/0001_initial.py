# Generated by Django 3.2.5 on 2021-07-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('image', models.URLField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('maker', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('content', models.CharField(max_length=15)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]
