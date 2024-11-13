# Generated by Django 5.1 on 2024-10-22 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0015_alter_paymentsinformation_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='paymentsinformation',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.paymentstatus'),
        ),
    ]
