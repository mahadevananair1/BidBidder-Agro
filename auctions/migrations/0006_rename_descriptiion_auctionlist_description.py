# Generated by Django 3.2.3 on 2021-05-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionlist_current_largest_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlist',
            old_name='descriptiion',
            new_name='description',
        ),
    ]
