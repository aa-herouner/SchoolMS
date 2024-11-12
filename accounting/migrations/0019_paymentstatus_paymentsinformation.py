# Generated by Django 5.1 on 2024-10-22 19:44

import django.db.models.deletion
import students.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0018_delete_paymentsinformation'),
        ('students', '0011_alter_studentinfo_class_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentsInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name=students.models.StudentInfo)),
                ('status', models.CharField(choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], default='unpaid', max_length=20)),
                ('class_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentclassinfo')),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.monthsoftheyear')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounting.academicsession')),
            ],
        ),
    ]
