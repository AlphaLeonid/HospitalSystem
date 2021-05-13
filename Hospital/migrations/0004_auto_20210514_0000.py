# Generated by Django 3.2 on 2021-05-13 16:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_auto_20210502_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='appointment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_time',
            field=models.CharField(choices=[('Morning', '上午'), ('Afternoon', '下午')], max_length=10),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='appointment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Hospital.appointment'),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='medicinerequest',
            unique_together={('diagnosis', 'medicine')},
        ),
    ]
