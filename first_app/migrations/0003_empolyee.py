# Generated by Django 4.0.2 on 2022-02-14 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_alter_student_managers_student_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empolyee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
    ]
