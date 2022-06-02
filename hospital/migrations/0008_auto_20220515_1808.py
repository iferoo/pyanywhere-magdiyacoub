# Generated by Django 3.2.13 on 2022-05-15 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_alter_patient_bed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.CharField(max_length=70)),
                ('Status', models.CharField(max_length=70)),
                ('RoomID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Beds', to='hospital.room')),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='Bed',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Patient', to='hospital.bed'),
        ),
        migrations.DeleteModel(
            name='Room_Bed',
        ),
    ]