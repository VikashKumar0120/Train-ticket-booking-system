from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='train_no',
        ),
        migrations.AddField(
            model_name='train',
            name='ac1_fare',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='train',
            name='ac2_fare',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='train',
            name='ac3_fare',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='train',
            name='cc_fare',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AlterField(
            model_name='train',
            name='arrival_time',
            field=models.DateTimeField(verbose_name='Arrival Date'),
        ),
        migrations.AlterField(
            model_name='train',
            name='departure_time',
            field=models.DateTimeField(verbose_name='Departure Date'),
        ),
        migrations.AlterField(
            model_name='train',
            name='train_no',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]