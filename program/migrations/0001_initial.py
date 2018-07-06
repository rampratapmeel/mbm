# Generated by Django 2.0.6 on 2018-07-04 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('course', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoPo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course_outcome', models.ForeignKey(on_delete=None, to='course.CourseOutcomes')),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('duration', models.DurationField()),
                ('department', models.ForeignKey(on_delete=None, to='department.Department')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.DateField()),
                ('active', models.BooleanField(default=False)),
                ('program', models.ForeignKey(on_delete=None, to='program.Program')),
            ],
        ),
        migrations.CreateModel(
            name='ProgramOutcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('title', models.CharField(max_length=150)),
                ('program', models.ForeignKey(on_delete=None, to='program.Program')),
            ],
        ),
        migrations.AddField(
            model_name='copo',
            name='program_outcome',
            field=models.ForeignKey(on_delete=None, to='program.ProgramOutcome'),
        ),
        migrations.AddField(
            model_name='copo',
            name='user',
            field=models.ForeignKey(on_delete=None, to='user.User'),
        ),
    ]
