# Generated by Django 2.0.2 on 2018-02-25 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OrderedMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example_app.Meal')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='ordered_meals', to='example_app.Order')),
            ],
        ),
    ]