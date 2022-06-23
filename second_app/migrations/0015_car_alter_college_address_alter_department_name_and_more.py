# Generated by Django 4.0.2 on 2022-02-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0014_remove_student_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('car_id', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.FloatField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='college',
            name='address',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='subjects',
            name='is_practical',
            field=models.BooleanField(null=True, verbose_name='ispractical'),
        ),
    ]
