# Generated by Django 5.0.2 on 2024-03-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticketRequest',
            field=models.TextField(null=True),
        ),
    ]
