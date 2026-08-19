from django.db import migrations


CONSULDENT_METRICS = "50 dentists reached, 3 test cohorts, payments active"

MULAKAT_POSTMORTEM = (
    "AI mock interviews generated from a job description. Stopped: people tried it "
    "once and didn't come back. Without repeat use there was no product to build on."
)

MENTAI_POSTMORTEM = (
    "a personalized mentorship app with daily guidance and adaptive tasks. Stopped "
    "after MVP testing: the users we spoke to didn't have the need we had designed for."
)


def set_copy(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent').update(metrics=CONSULDENT_METRICS)
    Project.objects.filter(slug='mulakat-pro').update(postmortem=MULAKAT_POSTMORTEM)
    Project.objects.filter(slug='mentai').update(postmortem=MENTAI_POSTMORTEM)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_consuldent_links'),
    ]

    operations = [
        migrations.RunPython(set_copy, noop),
    ]
