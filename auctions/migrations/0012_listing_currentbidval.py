# Generated by Django 4.0.1 on 2022-07-30 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_bid_bidder_remove_comment_commenter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='currentBidVal',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
