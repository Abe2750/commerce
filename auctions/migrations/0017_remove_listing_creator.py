# Generated by Django 4.0.1 on 2022-07-31 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='creator',
        ),
    ]
