from django.db import migrations, models


CONSULDENT_DESCRIPTION = (
    "ConsulDent is a clinical AI assistant for dentists, live on the App Store. "
    "Every answer is grounded in retrievable clinical sources — books, guidelines, "
    "reference documents — instead of model intuition, and comes back as structured "
    "output that fits the actual workflow: visit preparation, treatment explanations, "
    "clinical notes, patient communication. Voice input handles the reality of a "
    "clinic, where typing mid-procedure isn't an option. Under the hood it is a "
    "backend-first system: RAG pipelines, agent-style reasoning flows, and structured "
    "outputs rather than a chat box."
)


def apply_statuses(apps, schema_editor):
    Project = apps.get_model('main', 'Project')

    # One active project; everything else archived (default).
    Project.objects.filter(slug='consuldent').update(
        status='active',
        title='ConsulDent',
        description=CONSULDENT_DESCRIPTION,
    )

    # Dead domains — a dead link costs more credibility than an omitted one.
    Project.objects.filter(slug='mentai').update(demo_link='', title='MentAI')
    Project.objects.filter(slug='mulakat-pro').update(demo_link='', title='mulakat.pro')


def revert_statuses(apps, schema_editor):
    # Old featured flag is gone; nothing sensible to restore.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(
                choices=[
                    ('active', 'Active — currently building'),
                    ('work', 'Day job / internal'),
                    ('archived', 'Archived — stopped'),
                ],
                default='archived',
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='metrics',
            field=models.CharField(
                blank=True,
                help_text="Comma-separated proof points. e.g. '12 dentists in cohort, live on App Store, payments active'",
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='postmortem',
            field=models.CharField(
                blank=True,
                help_text='One sentence: why this stopped. Shown on archived projects.',
                max_length=200,
            ),
        ),
        migrations.AddField(
            model_name='project',
            name='app_store_link',
            field=models.URLField(blank=True),
        ),
        migrations.RemoveField(
            model_name='project',
            name='is_featured',
        ),
        migrations.RunPython(apply_statuses, revert_statuses),
    ]
