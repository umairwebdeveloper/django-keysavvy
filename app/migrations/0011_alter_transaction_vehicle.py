# Generated by Django 4.2.16 on 2024-12-03 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_transaction_vehicle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.vehicle'),
        ),
    ]
