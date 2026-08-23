from django.db import migrations


# The CV's diagnosis replaces the observation: the funnel was the problem.
NEW = ("AI mock interviews generated from a job description. Stopped: the "
       "bottleneck in the market was getting interviews, not preparing for them.")

OLD = ("AI mock interviews generated from a job description. Stopped: people tried "
       "it once and didn't come back. Without repeat use there was no product to build on.")


def reword(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='mulakat-pro').update(
        postmortem=NEW, short_description=NEW)


def revert(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='mulakat-pro').update(
        postmortem=OLD, short_description=OLD)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_cv_alignment'),
    ]

    operations = [
        migrations.RunPython(reword, revert),
    ]
