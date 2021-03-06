# Generated by Django 3.0.8 on 2020-08-10 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    # next line is added
    # DEFAULT_AUTO_FIELD='django.db.models.AutoField'  
    dependencies = [
        ('auctions', '0013_item_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
