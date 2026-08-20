from django.db import migrations, models


SHORT_DESCRIPTIONS = {
    'consuldent': (
        "A clinical AI assistant for dentists, live on the App Store. Answers come "
        "from retrievable clinical sources and land as structured output that fits "
        "the clinic's day: visit preparation, clinical notes, patient communication."
    ),
    # Stopped projects: last sentence matches the homepage postmortem verbatim.
    'mulakat-pro': (
        "AI mock interviews generated from a job description. Stopped: people tried "
        "it once and didn't come back. Without repeat use there was no product to build on."
    ),
    'mentai': (
        "A personalized mentorship app with daily guidance and adaptive tasks. Stopped "
        "after MVP testing: the users we spoke to didn't have the need we had designed for."
    ),
}


def curate(apps, schema_editor):
    Project = apps.get_model('main', 'Project')

    # Bootcamp exercises leave the curated list (they stay on GitHub).
    Project.objects.filter(slug__in=[
        'data-science-practices-repository',
        'basic-collaborative-filtering-model',
    ]).delete()

    for slug, text in SHORT_DESCRIPTIONS.items():
        Project.objects.filter(slug=slug).update(short_description=text)

    # MentAI: true year is 2024 (About and detail already say so); tech stack
    # normalized; profile/Instagram links removed — no working external link.
    Project.objects.filter(slug='mentai').update(
        year='2024',
        tech_stack='Python, LangChain, Firebase, GCP, Flutter',
        github_link='',
        other_link='',
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_consuldent_screenshot'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='short_description',
            field=models.CharField(
                blank=True,
                help_text='2-3 sentences for the projects index; the detail page keeps the long description.',
                max_length=280,
            ),
        ),
        migrations.RunPython(curate, noop),
    ]
