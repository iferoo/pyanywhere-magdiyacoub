# Generated by Django 3.2.13 on 2022-05-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0012_alter_patient_registerdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='OtherDiseases',
            field=models.DateField(max_length=70, null=True),
        ),
    ]
