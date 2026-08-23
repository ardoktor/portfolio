from django.db import migrations


def align(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    # Tech line aligned with the CV and the detail page: it's React Native,
    # and the backend story is Django (one codebase), not FastAPI.
    Project.objects.filter(slug='consuldent').update(
        tech_stack='Python, Django, React Native, RAG, pgvector, Whisper')


def revert(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent').update(
        tech_stack='Python, RAG, LLM Integration, FastAPI, React')


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_soft_metrics'),
    ]

    operations = [
        migrations.RunPython(align, revert),
    ]
