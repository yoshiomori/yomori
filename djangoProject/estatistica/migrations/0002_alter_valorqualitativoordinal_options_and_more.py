# Generated by Django 4.0.6 on 2022-08-19 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estatistica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valorqualitativoordinal',
            options={},
        ),
        migrations.CreateModel(
            name='GraficoBarrasParaVariaveisQualitativasOrdinais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=255)),
                ('quantidade', models.PositiveIntegerField()),
                ('variavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estatistica.variavelqualitativoordinal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GraficoBarrasParaVariaveisQualitativasNominais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=255)),
                ('quantidade', models.PositiveIntegerField()),
                ('variavel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estatistica.variavelqualitativonominal')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
