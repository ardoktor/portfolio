from django.db import migrations


# The cohort number is honest-soft: "~50", matching the detail page's prose.
METRICS = "~50 dentists reached, 3 test cohorts, payments active"


def soften(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent').update(metrics=METRICS)


def harden(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent').update(
        metrics="50 dentists reached, 3 test cohorts, payments active")


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_mulakat_note'),
    ]

    operations = [
        migrations.RunPython(soften, harden),
    ]
