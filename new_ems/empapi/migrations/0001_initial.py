# Generated by Django 3.0 on 2020-07-04 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=25)),
                ('photo', models.ImageField(default='pic/1.jpg', upload_to='pic')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.SmallIntegerField()),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'employee',
            },
        ),
    ]
