# Generated by Django 4.0 on 2022-01-01 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PictureInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene', models.CharField(max_length=100)),
                ('identifier', models.IntegerField()),
                ('slide', models.IntegerField()),
                ('imgsrc', models.CharField(max_length=600)),
                ('mutated', models.BooleanField(verbose_name='mutation present')),
                ('comment', models.CharField(max_length=450)),
                ('submission', models.DateTimeField(verbose_name='date logged')),
                ('author', models.CharField(max_length=150)),
                ('wildtype', models.BooleanField(verbose_name='wildtype')),
                ('center', models.CharField(choices=[('0750', '750'), ('0775', '775'), ('0800', '800'), ('0825', '825'), ('0850', '850'), ('0875', '875'), ('0900', '900'), ('0925', '925'), ('0950', '950')], max_length=32)),
                ('leftPresent', models.BooleanField(verbose_name='left gland beginning present')),
                ('leftBeginning', models.CharField(choices=[('0750', '750'), ('0775', '775'), ('0800', '800'), ('0825', '825'), ('0850', '850'), ('0875', '875'), ('0900', '900'), ('0925', '925'), ('0950', '950')], max_length=32)),
                ('rightPresent', models.BooleanField(verbose_name='right gland beginning present')),
                ('rightBeginning', models.CharField(choices=[('0750', '750'), ('0775', '775'), ('0800', '800'), ('0825', '825'), ('0850', '850'), ('0875', '875'), ('0900', '900'), ('0925', '925'), ('0950', '950')], max_length=32)),
            ],
        ),
    ]
