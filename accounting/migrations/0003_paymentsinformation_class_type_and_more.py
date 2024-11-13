# Generated by Django 5.1 on 2024-10-17 12:46

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_remove_paymentsinformation_class_type_and_more'),
        ('students', '0010_alter_studentinfo_class_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentsinformation',
            name='class_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='students.studentclassinfo'),
        ),
        migrations.AddField(
            model_name='paymentsinformation',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='StudentInfo',
        ),
    ]
