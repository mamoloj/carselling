# Generated by Django 4.0.3 on 2022-03-25 17:32

import car.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=120)),
                ('make', models.CharField(max_length=120)),
                ('model', models.CharField(max_length=120)),
                ('year', models.CharField(choices=[(2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002)], max_length=32)),
                ('condition', models.CharField(choices=[('poor', 'Poor'), ('fair', 'Fair'), ('good', 'Good'), ('excellent', 'Excellent')], max_length=32)),
                ('price', car.models.IntegerRangeField()),
            ],
        ),
    ]
