# Generated by Django 5.0.3 on 2024-03-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_books_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='owner',
            field=models.CharField(max_length=50),
        ),
    ]
