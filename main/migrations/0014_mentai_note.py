from django.db import migrations


TITLE = "We built a mentorship app without a mentor"
SLUG = "we-built-a-mentorship-app-without-a-mentor"
DATE = "2026-08-21"

TEXT = """MentAI started with a problem I had.

I was trying to lose weight. I was trying to get better at my job. I had a list of things I wanted to become, and most weeks I could not hold focus long enough to move on any of them. The gap between having a goal and doing anything about it felt like a solvable problem, and I was an engineer, so I tried to solve it.

The idea was a bridge between a person and their goal. Not a habit tracker — a guided path. You picked a journey and the app walked you through it over forty-five days: summaries of books that fit where you were, curated content, and the main feature, a personalized letter delivered every day.

> *Day fourteen of your weight loss journey. Here is what matters today.*

We built two tracks, losing weight and building a reading habit. Each was a curated path with a timeline, generated content, and a habit checkbox you could tick off. We collected your mood and what was going on with you, and the letters were supposed to adapt to it.

## Who built it

Seven of us, all friends, most from electrical engineering. One built the mobile app in Flutter. One handled product and project management. One ran marketing, another designed everything we posted. A therapist advised us as a volunteer. I did the backend, the system design, and the AI work — OpenAI's API, the generation pipeline, the scheduling, the infrastructure.

Most of us were engineers who did not like our day jobs and wanted to build something. That is a real reason to start a company and a bad reason to pick a particular company, though I did not know that yet.

Three or four months on design. Another six on building. Around ten months, all of it on evenings and weekends.

## What actually happened

We put it on TestFlight. Around twenty friends tried it. It never reached the App Store.

The letters became annoying.

That sounds like a small thing. It was the entire failure. The app arrived every day with something to tell you about your journey, and it had no idea who it was talking to on that particular day. You come home from work, you have had a terrible day, you are exhausted — and here is a letter explaining what you should be remembering about discipline. We collected mood inputs, but collecting a mood is not the same as knowing someone.

At some point they just felt like stupid letters.

And here is the part I could have noticed much earlier: I did not like them either. I was the target user. I had built the thing for my own problem. And I was not reading my own product's core feature, because the content was not good.

The habit tracking went the same way. Friends ticked a few boxes for a couple of days as a favour to us, and then stopped. It was a beautifully designed app. It was not a real product.

Meanwhile the Instagram account had around four thousand followers. We had a designer making posts, someone running the account, and an audience that kept growing. Four thousand people following a product that twenty people had tried and none of them wanted.

The standard advice is to build an audience before you build a product. We did that. It did not help, and it took me a long time to work out why.

The audience we built was general. Four thousand people interested in self-improvement is four thousand people who like reading about self-improvement. It is not a group of people who share one specific problem urgently enough to change what they do about it. We were producing content that performed well and selected for exactly the wrong thing — people who enjoy the topic, rather than people stuck on a particular task.

I think the advice is right and we applied it at the wrong resolution. The question is not how many people follow you. It is whether the people following you have the same problem as each other, and whether that problem is specific enough to build one thing for.

ConsulDent has nothing like four thousand followers. It has around fifty dentists across three test cohorts, all doing the same job, all hitting the same friction in the same week. That group is worth more than the audience we spent a year building, and it is smaller by two orders of magnitude.

## Why it failed

The architecture was not the problem. Neither was the team.

The problem was that we were generating mentorship content and none of us knew anything about mentorship.

What MentAI needed was someone with a real program — a coach, a domain expert, someone who had actually walked people through losing weight or building a reading habit and knew what to say on day fourteen when someone wants to quit. Our job would have been to take that person's method and build the system that delivered it at scale, adapted to each user.

Instead, seven engineers and a designer wrote the mentorship ourselves. We produced content in a domain where we had no standing. The letters were bad because we had nothing to say, and no amount of prompt engineering fixes having nothing to say.

The therapist advising us was volunteering her time, and she was generous with it. That is still not the same as having the expertise inside the product.

There is also a version of this that was just too early. This was before the models were as capable as they are now, and a lot of what we shipped was, in practice, a fairly bad implementation of an email subscription. Some of that gap would close today. Most of it would not.

## When we stopped

A couple of months after TestFlight. There was no single meeting where we decided.

People got busy. There was no money and no signal, so there was nothing to replace the motivation we had started with. Focus drifted. Eventually I was the only one still pushing, and being the last person pushing is its own kind of answer. At some point we said it out loud: none of us needed this product. It had never helped any of us. That was the end of it.

I think we could have said that earlier. The evidence was in my own behaviour months before I was willing to name it.

## What it was worth

I want to be careful here, because the tidy version of this story is that it was all a valuable lesson, and that flattens what it actually was.

MentAI is where I learned how software lives. Before it I was a network engineer who wrote scripts. Through it I learned what an API actually is, how OpenAI's API works, what serverless means, what Google Cloud Functions do, how something gets deployed and stays running without anyone touching it. That sounds basic written down. It was not basic to me then, and I do not think there is a way to learn it that does not involve building something real and watching it fail in production.

It was also my entrance ticket to a world I had no access to. We worked out of an incubation centre. We pitched to investors more than once. We went to entrepreneurship events and met founders and sat in rooms I would not otherwise have been in. None of it turned into a company, and all of it changed what I thought was available to me.

Ten months, seven people, four thousand followers, twenty testers, zero users. And the foundation for everything I have built since.

## I still think the problem is real

This is the part I am least sure about, so I will say it carefully.

I do not think we were wrong that the problem exists. Self-regulation, doing the thing you decided to do, staying in a relationship with your own goals — that is a real and old problem. Philosophers and writers have been circling it for centuries, which is a decent sign that it is not trivial and also that nobody has closed it.

What I think now is that daily personalized letters were the wrong shape for it. Something closer to a self-accountability structure would work better: defined periods, a clear sense of which phase you are in, a mechanism that helps you notice what you are not managing to do rather than one that tells you what to feel about it. Less motivational content, more understanding — and a healthier relationship with the goal than "here is day fourteen, keep going."

But there is a harder issue underneath, and it is the one that would make me hesitate before starting this again. The problem is vague. It is not obviously measurable and it is not obviously scalable. And the audience matters enormously — not everyone wants to become a better version of themselves. Most people, most of the time, want to have a good time and forget about it for a while. Building for the minority who genuinely want structure is a real business, but you have to know that is who you are building for, and we did not.

## What I took from it

The general lesson — validate before you build — is true and too vague to act on. The specific one is sharper:

**Do not build a product in a domain where you have no expertise and cannot bring any into the room.**

Not talk to users. Not do research. Have the expertise inside the product. If what you are selling is knowledge, someone on the team has to actually have it.

I did not fully apply this on the next attempt. [mulakat.pro](/projects/mulakat-pro/) had a similar shape in a different domain and failed for a different reason — that is a separate post.

It took until the third one. [ConsulDent](/projects/consuldent/) is built with a practising dentist as a co-founder rather than an advisor, and every clinical decision goes through someone who treats patients. That is the direct inheritance from this failure, and it is why the third one is still running."""


def add_note(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    Tag = apps.get_model('main', 'Tag')
    tag, _ = Tag.objects.get_or_create(name='MentAI')
    if not BlogPost.objects.filter(slug=SLUG).exists():
        BlogPost.objects.create(
            title=TITLE, slug=SLUG, text=TEXT, tag=tag, is_published=True,
        )
        # auto_now_add stamps insert time; set the authored date explicitly
        BlogPost.objects.filter(slug=SLUG).update(created_at=f'{DATE}T09:00:00Z')


def remove_note(apps, schema_editor):
    apps.get_model('main', 'BlogPost').objects.filter(slug=SLUG).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_projects_curation'),
    ]

    operations = [
        migrations.RunPython(add_note, remove_note),
    ]
