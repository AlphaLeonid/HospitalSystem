# Generated by Django 3.2 on 2021-05-02 04:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('appointment_time', models.DateTimeField()),
                ('isActive', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('detail', models.TextField()),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.appointment')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('inventory', models.IntegerField()),
                ('unit', models.CharField(choices=[('g', '克'), ('ml', '毫升'), ('box', '盒')], max_length=10)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='register_time',
            new_name='create_time',
        ),
        migrations.AddField(
            model_name='doctor',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MedicineRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('diagnosis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.diagnosis')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.medicine')),
            ],
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.doctor'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Hospital.patient'),
        ),
    ]
