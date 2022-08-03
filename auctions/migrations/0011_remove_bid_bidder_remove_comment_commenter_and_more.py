# Generated by Django 4.0.1 on 2022-07-24 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_bid_bidder_comment_commenter_listing_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidder',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='owner',
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('watchList', models.ManyToManyField(to='auctions.Listing')),
            ],
        ),
    ]
