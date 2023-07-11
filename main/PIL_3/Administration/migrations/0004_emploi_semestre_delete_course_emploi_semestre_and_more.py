# Generated by Django 4.2.3 on 2023-07-05 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0003_delete_administration_course_masse_horraire_utilisee_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emploi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.salle')),
                ('filiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.filiere')),
            ],
        ),
        migrations.CreateModel(
            name='Semestre',
            fields=[
                ('type_semestre', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.AddField(
            model_name='emploi',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.semestre'),
        ),
        migrations.AddField(
            model_name='emploi',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.matiere'),
        ),
        migrations.AddField(
            model_name='emploi',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administration.professeur'),
        ),
    ]
