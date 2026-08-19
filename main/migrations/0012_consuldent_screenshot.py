from django.db import migrations


SCREENSHOT_URL = "/static/main/img/consuldent-screenshot.png"


def set_screenshot(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent').update(image_url=SCREENSHOT_URL)


def unset_screenshot(apps, schema_editor):
    Project = apps.get_model('main', 'Project')
    Project.objects.filter(slug='consuldent', image_url=SCREENSHOT_URL).update(image_url='')


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_homepage_copy'),
    ]

    operations = [
        migrations.RunPython(set_screenshot, unset_screenshot),
    ]
