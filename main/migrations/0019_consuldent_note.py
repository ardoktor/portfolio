from django.db import migrations


TITLE = "Why we're building ConsulDent"
SLUG = "why-were-building-consuldent"
DATE = "2026-09-19"

TEXT = """A patient walks in. Everything looks routine. You are about to start the procedure and you find out they have Hepatitis C.

That changes the next hour. There is a transmission risk, so the protective equipment changes, the instrument handling changes, the whole setup around the chair changes. You remember most of this from school. You have not seen a case in five years. You are the only dentist in the clinic right now. You text a friend, but she has a patient in her chair too. Your patient is sitting there, waiting for you to remember.

That is the moment we built ConsulDent for.

## What it actually is

ConsulDent is a clinical copilot for dentists. Instead of digging through a textbook you cannot find, you ask the question and get an answer grounded in the literature, with the source attached.

Mid procedure you forget a dose. You check it with a calculator that was not built for guesswork: what is safe for a five year old with a penicillin allergy. The procedure ends and the patient needs to remember what happens next, so you hand them a document written for their case. What was done, what the treatment involves, what to watch for.

That is the product. It is not a clinic management system, and that distinction turned out to be the most important decision we made.

## Why not just use ChatGPT

It is a fair question and the honest answer is that you can. You just do not get four things.

You do not know what the answer is based on. We do not answer at all when the similarity score is not high enough, and when we do answer you can see which reference it came from. Dosage is the second one. In a general chat you recalculate from scratch every time, while ours is deterministic, running against a verified database that we deliberately keep outside the model. The third is that the answer dissolves. Even a good answer disappears into a conversation log, untagged and uncategorized, so you cannot find it again next month. And the fourth is that you still have to write the patient document yourself.

Dentists understood this immediately. That was the first real signal that we were solving something that existed.

## Who I am building it with

This is my third product. [MentAI](/projects/mentai/) was too crowded, seven people building an MVP for a need that turned out not to be there. [Mulakat Pro](/projects/mulakat-pro/) was too lonely, solo, and aimed at a bottleneck that was not the real bottleneck in that market.

This time I convinced my best friend, who is a dentist. That turned out to be the difference between the first two and this one.

> Putting a domain expert in the middle of the system and building the RAG architecture around them is not a nice to have. It is the architecture.

I have someone I can ask an unlimited number of stupid questions, someone who catches a wrong answer before a user does. That collapses the feedback loop from weeks into minutes. And because she owns the outcome too, I get into rooms I would never get into alone, which in this industry means other dentists.

## The positioning decision

I spent a lot of time in her clinic, looking for workflows where AI actually fits. One of the first ideas was patient onboarding. Take everything that happens before the chair, the history, the medications, the allergies, the intake conversation, and let the system structure it.

It is a real problem and we will come back to it. But the moment you own patient intake, your obligations change and your scope changes with them. You are not a clinical tool anymore. You are a clinic management system, which means appointments, records, billing and compliance.

That market is a red ocean. Established players, salespeople in the field, and a painful infrastructure migration for anyone who wants to switch. Our competitive advantage there was zero.

So we said no for now. No to owning intake, no to image analysis, no to becoming another clinic management system. The layer worth owning first was clinical intelligence itself, the thirty seconds where a dentist needs a trustworthy answer with a patient in the chair. Intake comes later, on top of that layer, not instead of it.

That decision also moved us off the desktop. An assistant walking to a computer to look something up is not a real workflow. It had to work chairside, on a tablet or a phone, standing up, between patients.

## Where we are now

Around sixty dentists have used it across three cohorts. Three quarters of them asked at least one real clinical question. Half took a second action, saving an answer, turning it into a note or generating a document. A third came back on a different day.

We are far from product market fit. What we have is an MVP with real clinical usage and metrics we defined ourselves, which is more than we had six months ago and less than we need.

Along the way we improved answer quality, cut response time, deepened the RAG structure, built agentic workflows, watched people use it, and redesigned the same screens more times than I would like to admit.

## Why I am writing this

This industry moves quickly and I am building in it at night and on weekends, with a full time job. Writing forces me to be clear about what I am actually doing and why.

The next posts get more technical. Evaluation, response quality against latency, the RAG incidents we ran into in production. Distribution and marketing too, as they happen, because we are figuring that part out on the fly.

Thanks for reading this far."""

# The post says "around sixty dentists" — the site's metrics strip follows.
NEW_METRICS = "~60 dentists reached, 3 test cohorts, payments active"
OLD_METRICS = "~50 dentists reached, 3 test cohorts, payments active"


def add_note(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    Tag = apps.get_model('main', 'Tag')
    Project = apps.get_model('main', 'Project')
    tag, _ = Tag.objects.get_or_create(name='ConsulDent')
    if not BlogPost.objects.filter(slug=SLUG).exists():
        BlogPost.objects.create(
            title=TITLE, slug=SLUG, text=TEXT, tag=tag, is_published=True,
        )
        BlogPost.objects.filter(slug=SLUG).update(created_at=f'{DATE}T09:00:00Z')
    Project.objects.filter(slug='consuldent').update(metrics=NEW_METRICS)


def remove_note(apps, schema_editor):
    apps.get_model('main', 'BlogPost').objects.filter(slug=SLUG).delete()
    apps.get_model('main', 'Project').objects.filter(slug='consuldent').update(
        metrics=OLD_METRICS)


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_mulakat_postmortem_wording'),
    ]

    operations = [
        migrations.RunPython(add_note, remove_note),
    ]
