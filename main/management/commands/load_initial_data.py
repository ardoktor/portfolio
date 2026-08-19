from django.core.management.base import BaseCommand
from main.models import Project, Tag


CONSULDENT_DESCRIPTION = (
    "ConsulDent is a clinical AI assistant for dentists, live on the App Store. "
    "Every answer is grounded in retrievable clinical sources — books, guidelines, "
    "reference documents — instead of model intuition, and comes back as structured "
    "output that fits the actual workflow: visit preparation, treatment explanations, "
    "clinical notes, patient communication. Voice input handles the reality of a "
    "clinic, where typing mid-procedure isn't an option. Under the hood it is a "
    "backend-first system: RAG pipelines, agent-style reasoning flows, and structured "
    "outputs rather than a chat box."
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
                'demo_link': 'https://consuldent.com',
                # TODO(owner): metrics (real numbers only) and app_store_link
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
                # TODO(owner): one-sentence postmortem
                'order': 2,
            },
            {
                'title': 'MentAI',
                'slug': 'mentai',
                'status': 'archived',
                'description': 'MentAI is a personalized mentorship application designed to help users achieve their cognitive, emotional, and productivity goals through daily guidance, structured tasks, and adaptive content.',
                'year': '2025',
                'tech_stack': 'Python, LangChain, Firebase, GCP, Flutter',
                # demo_link intentionally empty: mentai.app is offline
                # TODO(owner): one-sentence postmortem
                'github_link': 'https://github.com/ardoktor',
                'other_link': 'https://www.instagram.com/mentai.app/',
                'order': 3,
            },
            {
                'title': 'Data Science Practices Repository',
                'slug': 'data-science-practices-repository',
                'status': 'archived',
                'description': 'A curated collection of hands-on data science mini-projects covering data analysis, machine learning, deep learning, and storytelling with data.',
                'year': '2021',
                'tech_stack': 'Python, TensorFlow, Pandas, Hugging Face, SQL, CNN',
                'github_link': 'https://github.com/ardoktor/DataSciencePractises/tree/main',
                'order': 10,
            },
            {
                'title': 'Basic Collaborative Filtering Model',
                'slug': 'basic-collaborative-filtering-model',
                'status': 'archived',
                'description': 'A basic collaborative filtering recommendation system using Microsoft recommenders library with MovieLens dataset.',
                'year': '2021',
                'tech_stack': 'Python, NumPy, Sklearn',
                'github_link': 'https://github.com/ardoktor/RecommenderSystems/blob/main/huaweiReccomenderv3.ipynb',
                'order': 11,
            },
        ]

        for p_data in projects:
            Project.objects.get_or_create(
                slug=p_data['slug'],
                defaults=p_data
            )
            self.stdout.write(f'  Created: {p_data["title"]}')

        self.stdout.write(self.style.SUCCESS(f'Done! {Project.objects.count()} projects loaded.'))
