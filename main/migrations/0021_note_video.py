from django.db import migrations


SLUG = "why-were-building-consuldent"
BASE = "https://pub-8662b4f421c24dd3a0f306aec1a2151d.r2.dev"

ANCHOR = "## Why I am writing this"

SECTION = """## A walkthrough

Eleven minutes through the product and the system behind it: the four tools, how a question gets routed, and how we check the answers.

<video controls preload="none"
       poster="{base}/consuldent-architecture-poster.jpg"
       src="{base}/consuldent-architecture.mp4"></video>
<p class="caption">Architecture, routing and evaluation &middot; September 2026</p>

""".format(base=BASE)


def add_video(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        if '<video' in post.text:
            continue
        post.text = post.text.replace(ANCHOR, SECTION + ANCHOR, 1)
        post.save(update_fields=['text'])


def remove_video(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        post.text = post.text.replace(SECTION, '', 1)
        post.save(update_fields=['text'])


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_note_game_plan_quote'),
    ]

    operations = [
        migrations.RunPython(add_video, remove_video),
    ]
