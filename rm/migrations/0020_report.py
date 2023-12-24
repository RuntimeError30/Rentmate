# Generated by Django 4.1.5 on 2023-05-01 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rm', '0019_remove_waitforapproval_id_alter_waitforapproval_apps'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob', models.CharField(max_length=100, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rm.pro_owner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rm.residant')),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]
