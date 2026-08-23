from django.core.management.base import BaseCommand
from main.models import Project, Tag


CONSULDENT_DESCRIPTION = (
    "ConsulDent is a clinical AI assistant for dentists, live on the App Store. "
    "It answers from retrievable clinical sources — guidelines, books, reference "
    "documents — and returns structured output that fits the workflow: visit "
    "preparation, clinical notes, patient communication. Under the hood: RAG "
    "pipelines and agent-style reasoning instead of a chat box."
)


class Command(BaseCommand):
    help = 'Load initial project data'

    def handle(self, *args, **options):
        if Project.objects.exists():
            self.stdout.write(f'Projects already exist: {Project.objects.count()}')
            return

        self.stdout.write('Creating initial data...')

        # Create tags
        Tag.objects.get_or_create(name='ConsulDent')
        Tag.objects.get_or_create(name='MentAI')
        Tag.objects.get_or_create(name='mulakat.pro')

        # Create projects — exactly one may be "active" at a time.
        projects = [
            {
                'title': 'ConsulDent',
                'slug': 'consuldent',
                'status': 'active',
                'description': CONSULDENT_DESCRIPTION,
                'year': '2024',
                'tech_stack': 'Python, RAG, LLM Integration, FastAPI, React',
                'short_description': "A clinical AI assistant for dentists, live on the App Store. Answers come from retrievable clinical sources and land as structured output that fits the clinic's day: visit preparation, clinical notes, patient communication.",
                'demo_link': 'https://consuldent.app',
                'app_store_link': 'https://apps.apple.com/tr/app/consuldent/id6781041991',
                'metrics': '~50 dentists reached, 3 test cohorts, payments active',
                'image_url': '/static/main/img/consuldent-screenshot.png',
                'order': 1,
            },
            {
                'title': 'mulakat.pro',
                'slug': 'mulakat-pro',
                'status': 'archived',
                'description': 'An AI-powered interview preparation platform that generates personalized mock interviews based on job descriptions and user profiles. Features voice-based interaction and real-time feedback to simulate realistic interview scenarios.',
                'year': '2025',
                'tech_stack': 'Python, OpenAI API, LangChain, Django, Whisper',
                # demo_link intentionally empty: mulakat.pro domain has expired
                'postmortem': "AI mock interviews generated from a job description. Stopped: people tried it once and didn't come back. Without repeat use there was no product to build on.",
                'short_description': "AI mock interviews generated from a job description. Stopped: people tried it once and didn't come back. Without repeat use there was no product to build on.",
                'order': 2,
            },
            {
                'title': 'MentAI',
                'slug': 'mentai',
                'status': 'archived',
                'description': 'MentAI is a personalized mentorship application designed to help users achieve their cognitive, emotional, and productivity goals through daily guidance, structured tasks, and adaptive content.',
                'year': '2024',
                'tech_stack': 'Python, LangChain, Firebase, GCP, Flutter',
                # demo_link intentionally empty: mentai.app is offline
                'postmortem': "a personalized mentorship app with daily guidance and adaptive tasks. Stopped after MVP testing: the users we spoke to didn't have the need we had designed for.",
                'short_description': "A personalized mentorship app with daily guidance and adaptive tasks. Stopped after MVP testing: the users we spoke to didn't have the need we had designed for.",
                'order': 3,
            },
        ]

        for p_data in projects:
            Project.objects.get_or_create(
                slug=p_data['slug'],
                defaults=p_data
            )
            self.stdout.write(f'  Created: {p_data["title"]}')

        self.stdout.write(self.style.SUCCESS(f'Done! {Project.objects.count()} projects loaded.'))
