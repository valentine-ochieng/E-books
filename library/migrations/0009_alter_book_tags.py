# Generated by Django 3.2.9 on 2022-01-12 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_book_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='library.Tag'),
        ),
    ]
