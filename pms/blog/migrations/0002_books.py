# Generated by Django 5.0.1 on 2024-02-01 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('qty', models.IntegerField()),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]