# Generated by Django 4.2.5 on 2023-09-15 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_alter_books_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='books',
            name='publisher',
            field=models.CharField(max_length=200),
        ),
    ]
