# Generated by Django 4.0.4 on 2022-04-25 12:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0011_alter_cart_food_alter_cart_quantity_alter_cart_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
                ('address_type', models.CharField(default='Home', max_length=10)),
                ('city_name', models.CharField(max_length=50)),
                ('country_name', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=6)),
                ('user_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_name', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Addresses',
            },
        ),
    ]
