# Generated by Django 4.1.5 on 2023-04-29 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0009_alter_pro_owner_otp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro_owner',
            name='twofact',
            field=models.CharField(default='TURNED OFF', max_length=10),
        ),
    ]