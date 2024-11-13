# Generated by Django 5.1 on 2024-10-17 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_alter_studentinfo_class_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='class_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students_students', to='students.studentclassinfo'),
        ),
    ]
