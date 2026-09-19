from django.db import migrations


SLUG = "why-were-building-consuldent"

OLD = ("> Putting a domain expert in the middle of the system and building the RAG "
       "architecture around them is not a nice to have. It is the architecture.")

NEW = ("> The game plan is simple: put a domain expert at the center and build the RAG "
       "architecture around her. Reach people through the cheapest channel available, "
       "listen to what they say, watch what they do, make the product better. Repeat.")


def reword(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        post.text = post.text.replace(OLD, NEW)
        post.save(update_fields=['text'])


def revert(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    for post in BlogPost.objects.filter(slug=SLUG):
        post.text = post.text.replace(NEW, OLD)
        post.save(update_fields=['text'])


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_consuldent_note'),
    ]

    operations = [
        migrations.RunPython(reword, revert),
    ]
