# Generated by Django 5.2 on 2025-04-16 11:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="movie",
            table="movies_movie",
        ),
    ]
