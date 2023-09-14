# Generated by Django 3.2 on 2023-04-28 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Apptment_Date', models.DateField()),
                ('Time_slot', models.TimeField()),
                ('Token', models.IntegerField()),
                ('Problem', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Appointment',
            },
        ),
        migrations.AlterField(
            model_name='patient_pay_tran',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]