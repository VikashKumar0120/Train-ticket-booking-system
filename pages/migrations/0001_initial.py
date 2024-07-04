from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.FloatField(blank=True, null=True)),
                ('AC1', models.CharField(max_length=100)),
                ('AC2', models.CharField(max_length=100)),
                ('AC3', models.CharField(max_length=100)),
                ('Sleeper', models.CharField(max_length=100)),
                ('General', models.CharField(max_length=100)),
                ('train_no', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_no', models.IntegerField(default=0)),
                ('PNR', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('distance', models.IntegerField(default=0)),
                ('coach', models.CharField(max_length=100)),
                ('fare', models.FloatField(blank=True, null=True)),
                ('arrival_time', models.DateTimeField(verbose_name='date published')),
                ('departure_time', models.DateTimeField(verbose_name='date published')),
                ('seat_no', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('train_no', models.IntegerField(default=0)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('distance', models.IntegerField(default=0)),
                ('arrival_time', models.DateTimeField(verbose_name='date published')),
                ('departure_time', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
