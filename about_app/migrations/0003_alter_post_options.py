# Generated by Django 4.2.16 on 2024-12-04 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_app', '0002_post_excerpt_post_updated_on'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
