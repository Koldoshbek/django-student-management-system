# Generated by Django 3.0.7 on 2021-05-18 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('subjects', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('question', models.CharField(max_length=256)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Survey')),
            ],
        ),
    ]
