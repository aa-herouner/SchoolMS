# Generated by Django 5.1 on 2024-10-22 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0014_alter_paymentsinformation_class_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentsinformation',
            name='status',
            field=models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20),
        ),
        migrations.DeleteModel(
            name='PaymentStatus',
        ),
    ]
