from django.db import migrations


BASE = "https://pub-8662b4f421c24dd3a0f306aec1a2151d.r2.dev"

SOURCE_SLUG = "why-were-building-consuldent"

# Exactly what 0021 inserted, so it can be lifted back out cleanly.
MOVED_SECTION = """## A walkthrough

Eleven minutes through the product and the system behind it: the four tools, how a question gets routed, and how we check the answers.

<video controls preload="none"
       poster="{base}/consuldent-architecture-poster.jpg"
       src="{base}/consuldent-architecture.mp4"></video>
<p class="caption">Architecture, routing and evaluation &middot; September 2026</p>

""".format(base=BASE)

TITLE = "How ConsulDent works, in eleven minutes"
SLUG = "how-consuldent-works-in-eleven-minutes"
DATE = "2026-09-19T11:00:00Z"

TEXT = """A screen recording instead of an essay: the product, the system behind it, and how we check that the answers hold up.

<video controls preload="none"
       poster="{base}/consuldent-architecture-poster.jpg"
       src="{base}/consuldent-architecture.mp4"></video>
<p class="caption">Architecture, routing and evaluation &middot; September 2026</p>

What it covers:

- The four tools and the job each one does: clinical query, prescription and dosing, post-op patient documents, literature search.
- How a question gets routed. Intent detection, the Turkish question rewritten into English search queries, retrieval running in parallel over the corpus.
- Where the language model is deliberately kept out. Dosage math runs as plain code over a verified drug database; the model only narrates the result.
- How answers get checked, and what "no source, no claim" looks like once it is a rule in the pipeline rather than a slogan.

The written version of the decisions behind all this is in [Why we're building ConsulDent](/blog/why-were-building-consuldent/).""".format(base=BASE)


def move_video(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    Tag = apps.get_model('main', 'Tag')

    for post in BlogPost.objects.filter(slug=SOURCE_SLUG):
        if MOVED_SECTION in post.text:
            post.text = post.text.replace(MOVED_SECTION, '', 1)
            post.save(update_fields=['text'])

    tag, _ = Tag.objects.get_or_create(name='ConsulDent')
    if not BlogPost.objects.filter(slug=SLUG).exists():
        BlogPost.objects.create(
            title=TITLE, slug=SLUG, text=TEXT, tag=tag, is_published=True,
        )
        BlogPost.objects.filter(slug=SLUG).update(created_at=DATE)


def undo(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG).delete()
    for post in BlogPost.objects.filter(slug=SOURCE_SLUG):
        if '<video' not in post.text:
            post.text = post.text.replace(
                "## Why I am writing this", MOVED_SECTION + "## Why I am writing this", 1)
            post.save(update_fields=['text'])


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_note_video'),
    ]

    operations = [
        migrations.RunPython(move_video, undo),
    ]
