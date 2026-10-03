from django.db import migrations


TITLE = "We put a threshold on a number that meant nothing"
SLUG = "we-put-a-threshold-on-a-number-that-meant-nothing"
DATE = "2026-10-02T09:00:00Z"

TEXT = """My co-founder kept telling me the answers were wrong. She is a dentist, she was testing the system every week, and she was not vague about it.

I had one number to check her against. Every passage the system retrieved came back with a similarity score, and the scores were low. I assumed that was normal for dense medical text.

It was not normal. It was the wrong operator. And it was not what she was complaining about.

Most writing about RAG is about how to build the pipeline. This is about what ours looked like once a real person was using it, and the things that went wrong that nobody had warned me about.

## Same passages, different number

What settled it was a side by side run. The same question went to two systems. One was the Supabase function we were shipping. The other was a local version doing plain cosine similarity in numpy. Same corpus, same embeddings.

|  | Supabase | Local |
| --- | --- | --- |
| Top passage | 14.2% | 63.2% |
| Third passage | 12.9% | 62.1% |

The third passage was word for word the same text in both. The generated answers were close to identical. Retrieval was working. The only thing that differed was the number attached to it.

## One character

```sql
-- before
1 - (document_embeddings.embedding <-> query_embedding) AS similarity
-- after
1 - (document_embeddings.embedding <=> query_embedding) AS similarity
```

In pgvector, `<->` is Euclidean distance and `<=>` is cosine distance. We were subtracting a Euclidean distance from one and calling the result a similarity.

OpenAI embeddings have unit length, and for unit vectors the two distances are tied together by a fixed formula:

```
d = sqrt(2 - 2 * cos(theta))
```

Put a cosine similarity of 0.632 in and you get a distance of 0.858. One minus that is 0.142. That is our 14.2 percent, to the decimal.

The same formula explains why nobody noticed. It only ever goes one direction, so the passage that ranks first under cosine also ranks first under Euclidean. Nothing crashed. No wrong passage came back. The answers read the same. The bug lived in a number that nothing visible depended on.

## What the number broke

The part that mattered was the refusal rule. In a clinical product, knowing when not to answer is the feature.

We had set a similarity threshold on the old scale, and on that scale it looked like a low bar. Translated into real cosine similarity, it sat just under our best results. It was far stricter than we intended.

So "no source, no claim" was resting on a number we could not interpret. The fix did not make retrieval better, because the same passages came back in the same order. What it gave us was a score we could finally reason about.

## What runs now

Cosine everywhere, and two thresholds instead of one.

The first decides which passages come back from the database at all. The second is higher, and it decides whether what came back is worth standing behind.

If every retrieved passage falls under the second one, the system does not try harder. It swaps the context for an instruction that says the sources hold no specific data on this, keep any general answer short, and do not make up a number, a dose or a percentage.

Two thresholds is deliberate. A passage can be good enough to show as a source and not good enough to build a dosage claim on. The explanation of the operator bug still sits at the top of the SQL file, so nobody puts it back.

## Turkish question, English corpus

This is the other thing nobody mentions. Dentists ask in Turkish, often the way a patient would say it. Every source in the corpus is an English textbook. That is a cross-lingual retrieval problem, and it shaped more of the pipeline than I expected.

A dentist types "Dişim çok ağrıyor, soğukta deliriyor". The textbook says "prolonged response to cold stimulus, possible irreversible pulpitis". Those two sentences mean the same thing and share no words.

The first fix was a separate translation stage in front of retrieval. That stage is gone now. The router does the job itself: it reads the Turkish question and writes two or three English clinical queries, each aimed at a different angle. Translation, clinical vocabulary and fan-out happen in one step. The answer comes back in Turkish whatever language the source was in.

## What she was actually right about

The operator fix changed a number. It did not change a single answer, which means it was never the thing she was pointing at.

The answers were weak for other reasons, and fixing them took several changes rather than one.

The first was changing the shape of generation. Instead of handing the model the passages and asking for an answer, the pipeline now pulls out the cited facts first and then writes from only those facts.

Then came retrieval. Each question now runs as several searches against the vector store instead of one, and the model gets more context to work from. We experimented with chunk sizes and settled on about 300 words with a 20 percent overlap. For the sources where plain text extraction was not enough, we added OCR as a fallback.

None of these was dramatic on its own. Together they are what improved the answers. And the signal that started all of it was a domain expert reading the output, which caught what none of our metrics could.

## What building RAG actually looks like

The tutorial version of RAG is four steps: chunk, embed, retrieve, generate. The version you live with is different. A score has to mean something before you can build a rule on it. Your users may not ask in the language your sources are written in. And weak answers are often not a retrieval problem at all.

These are the things you face when you build one. None of them showed up as an error. Each one showed up as a person saying the answer was not good enough.

None of this is finished. Optimization on a system like this is continuous. There is always a better chunk size, a sharper query or a stricter check, and we are still working on all of them."""


def add_note(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    Tag = apps.get_model('main', 'Tag')

    tag, _ = Tag.objects.get_or_create(name='ConsulDent')
    if not BlogPost.objects.filter(slug=SLUG).exists():
        BlogPost.objects.create(
            title=TITLE, slug=SLUG, text=TEXT, tag=tag, is_published=True,
        )
        # created_at is auto_now_add, so the real date has to go in afterwards
        BlogPost.objects.filter(slug=SLUG).update(created_at=DATE)


def undo(apps, schema_editor):
    BlogPost = apps.get_model('main', 'BlogPost')
    BlogPost.objects.filter(slug=SLUG).delete()


class Migration(migrations.Migration):
    """The pgvector operator post. The formula is written as plain text rather
    than a latex block: the site renders markdown only, so latex source would
    reach the reader unrendered."""

    dependencies = [
        ('main', '0023_video_ios'),
    ]

    operations = [
        migrations.RunPython(add_note, undo),
    ]
