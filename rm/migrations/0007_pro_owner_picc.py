# Generated by Django 4.1.5 on 2023-04-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0006_residant_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pro_owner',
            name='picc',
            field=models.ImageField(null=True, upload_to='bimg/'),
        ),
    ]
