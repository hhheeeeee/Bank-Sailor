# Generated by Django 4.2.4 on 2023-11-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_depositoption_intr_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savingproduct',
            name='dcls_end_day',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]