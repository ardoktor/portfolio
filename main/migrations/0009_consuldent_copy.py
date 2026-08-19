from django.db import migrations


# Two sentences on what it does, one on how it's built.
# The long-form story lives on the project detail page.
CONSULDENT_DESCRIPTION = (
    "ConsulDent is a clinical AI assistant for dentists, live on the App Store. "
    "It answers from retrievable clinical sources — guidelines, books, reference "
    "documents — and returns structured output that fits the workflow: visit "
    "preparation, clinical notes, patient communication. Under the hood: RAG "
    "pipelines and agent-style reasoning instead of a chat box."
)

# Owner-asserted facts only; the cohort number slots in front once supplied.
CONSULDENT_METRICS = "live on the App Store, payments active"


def tighten_copy(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent', metrics='').update(metrics=CONSULDENT_METRICS)
    Project.objects.filter(slug='consuldent').update(description=CONSULDENT_DESCRIPTION)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_project_status'),
    ]

    operations = [
        migrations.RunPython(tighten_copy, noop),
    ]
