# Generated by Django 3.0.2 on 2020-07-05 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('study_books', '0005_cart'),
    ]

    operations = [
        migrations.DeleteModel(
            name='books_college',
        ),
        migrations.DeleteModel(
            name='books_eng',
        ),
        migrations.DeleteModel(
            name='books_medical',
        ),
        migrations.DeleteModel(
            name='books_school',
        ),
        migrations.DeleteModel(
            name='cart',
        ),
    ]
