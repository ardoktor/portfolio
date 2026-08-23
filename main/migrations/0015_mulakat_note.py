from django.db import migrations


TITLE = "I built the wrong half of the problem"
SLUG = "i-built-the-wrong-half-of-the-problem"
DATE = "2026-08-21"

TEXT = """mulakat.pro came out of my own job search, and I built all of it alone.

This was right after [MentAI failed](/blog/we-built-a-mentorship-app-without-a-mentor/). That was a low period — ten months of work with six friends had ended in nothing, and I was interviewing while trying to figure out what to do next. Building something solo felt like the correct response at the time. It was at least a smaller thing to be wrong about.

I was grinding LeetCode. Reverse a linked list, binary search, bubble sort, graphs. And somewhere in the middle of it I hit a question I could not answer: when am I ready? There was no way to measure how prepared I was for any specific job. I was doing work with no visible relationship to the thing I was preparing for.

So I started pasting my CV and the job description into ChatGPT and asking where the gap was. That worked well enough that it looked like a product. Parse the CV, parse the job post, extract the delta, turn it into an ordered preparation plan, and let people practise against it. Four or five months of evenings.

## The first reason it failed

I solved a problem that arrives too late.

In Turkey, preparing for the interview is not the hard part. Getting the interview is. LinkedIn had become unusable — every posting collected thousands of applications within hours, and most people never got evaluated at all. Not rejected. Not interviewed badly. Just never looked at.

Against that, a tool that helps you prepare for an interview is solving something that only matters after you have already cleared the difficult step. I had built for the small group of people who got through, and I had built it as though the scarce resource was preparation. The scarce resource was attention from a human being on the other side.

That is the part I would want a younger version of me to sit with. The product worked. The reasoning behind it was sound. It just answered a question further down the funnel than the one people were actually stuck on.

## The second reason

People looking for a job are not willing to spend money.

This seems obvious written down. It was not obvious to me while building. I was asking for payment from people who had no income yet and no certainty about when they would. Every rupture in that group's life pushes spending down, and a preparation tool is exactly the kind of purchase that gets postponed indefinitely.

Wanting something and paying for it are different behaviours, and I had only tested the first one — on myself.

## The Reddit post

At some point I posted it to Reddit and got roasted.

Most of the criticism was about the UI and the site not working properly. Surface problems, technical ones, fixable. That stung more than it should have and it was also not the real issue — nobody in that thread told me I had built for the wrong stage of the funnel, because that is not what you notice from a landing page.

But it was the first time real strangers looked at something I made and told me what they actually thought, rather than being encouraging because they knew me. After MentAI, where twenty friends politely ticked a few boxes, that was worth something. Harsh feedback from people with no reason to be kind is more useful than warm feedback from people who love you.

## What it cost and what it changed

Four or five months, solo, during a period when I was not in good shape. I let the domain expire rather than renewing it, which is its own honest signal about where the project had landed.

What I took from it is narrower than the MentAI lesson and, I think, more useful.

With MentAI I learned not to build in a domain where nobody on the team has expertise. With [mulakat.pro](/projects/mulakat-pro/) I had domain knowledge — I was the user, I was actively interviewing, I understood the problem from the inside. That was not enough, because I had scoped the problem at the wrong point in the chain.

Being close to a problem tells you it exists. It does not tell you which part of it is the bottleneck, and it does not tell you whether the people with that problem will pay to have it solved. Those are separate questions and I had answered neither."""


def add_note(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    Tag = apps.get_model('main', 'Tag')
    tag, _ = Tag.objects.get_or_create(name='mulakat.pro')
    if not BlogPost.objects.filter(slug=SLUG).exists():
        BlogPost.objects.create(
            title=TITLE, slug=SLUG, text=TEXT, tag=tag, is_published=True,
        )
        BlogPost.objects.filter(slug=SLUG).update(created_at=f'{DATE}T10:00:00Z')


def remove_note(apps, schema_editor):
    apps.get_model('main', 'BlogPost').objects.filter(slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_mentai_note'),
    ]

    operations = [
        migrations.RunPython(add_note, remove_note),
    ]
