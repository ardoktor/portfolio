from django.db import migrations


APP_STORE_LINK = "https://apps.apple.com/tr/app/consuldent/id6781041991"
WEB_LINK = "https://consuldent.app"


def set_links(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    # Correct domain is consuldent.app (consuldent.com was wrong), plus the App Store URL.
    Project.objects.filter(slug='consuldent').update(
        app_store_link=APP_STORE_LINK,
        demo_link=WEB_LINK,
    )


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_consuldent_copy'),
    ]

    operations = [
        migrations.RunPython(set_links, noop),
    ]
