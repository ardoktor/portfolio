from django.db import migrations


SLUG = "how-consuldent-works-in-eleven-minutes"

OLD = '<video controls preload="none"'
NEW = '<video controls playsinline preload="metadata"'


def fix(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        post.text = post.text.replace(OLD, NEW)
        post.save(update_fields=['text'])


def undo(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        post.text = post.text.replace(NEW, OLD)
        post.save(update_fields=['text'])


class Migration(migrations.Migration):
    """iOS Safari shows a struck-through play icon when it has no metadata to
    go on, and without playsinline it hijacks the whole screen. metadata is a
    small range request thanks to faststart, so the page still costs almost
    nothing before playback."""

    dependencies = [
        ('main', '0022_video_note'),
    ]

    operations = [
        migrations.RunPython(fix, undo),
    ]
