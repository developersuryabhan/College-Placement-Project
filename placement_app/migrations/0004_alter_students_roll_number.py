# Generated by Django 4.2.7 on 2023-11-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement_app', '0003_alter_students_email_alter_students_gpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='roll_number',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
