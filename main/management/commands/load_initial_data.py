from django.core.management.base import BaseCommand
from main.models import Project, Tag


class Command(BaseCommand):
    help = 'Load initial project data'

    def handle(self, *args, **options):
        if Project.objects.exists():
            self.stdout.write(f'Projects already exist: {Project.objects.count()}')
            return

        self.stdout.write('Creating initial data...')

        # Create tags
        tag_consuldent, _ = Tag.objects.get_or_create(name='ConsulDent')
        tag_mentai, _ = Tag.objects.get_or_create(name='MentAI')
        tag_mulakat, _ = Tag.objects.get_or_create(name='mulakat.pro')

        # Create projects
        projects = [
            {
                'title': 'ConsulDent - Dental Knowledge Assistant',
                'slug': 'consuldent',
                'description': 'An AI-powered dental knowledge assistant that helps clinicians with patient case analysis, knowledge base search, and clinical decision support. Built with a RAG-based system for querying dental literature and presenting structured, evidence-based responses.',
                'year': '2024',
                'tech_stack': 'Python, RAG, LLM Integration, FastAPI, React',
                'demo_link': 'https://consuldent.com',
                'order': 1,
                'is_featured': True,
            },
            {
                'title': 'mulakat.pro - AI Interview Preparation',
                'slug': 'mulakat-pro',
                'description': 'An AI-powered interview preparation platform that generates personalized mock interviews based on job descriptions and user profiles. Features voice-based interaction and real-time feedback to simulate realistic interview scenarios.',
                'year': '2025',
                'tech_stack': 'Python, OpenAI API, LangChain, Django, Whisper',
                'demo_link': 'https://mulakat.pro',
                'order': 2,
                'is_featured': True,
            },
            {
                'title': 'MentAI - Personalized AI Mentorship Platform',
                'slug': 'mentai',
                'description': 'MentAI is a personalized mentorship application designed to help users achieve their cognitive, emotional, and productivity goals through daily guidance, structured tasks, and adaptive content.',
                'year': '2025',
                'tech_stack': 'Python, LangChain, Firebase, GCP, Flutter',
                'demo_link': 'https://mentai.app',
                'github_link': 'https://github.com/ardoktor',
                'other_link': 'https://www.instagram.com/mentai.app/',
                'order': 3,
                'is_featured': True,
            },
            {
                'title': 'Data Science Practices Repository',
                'slug': 'data-science-practices-repository',
                'description': 'A curated collection of hands-on data science mini-projects covering data analysis, machine learning, deep learning, and storytelling with data.',
                'year': '2021',
                'tech_stack': 'Python, TensorFlow, Pandas, Hugging Face, SQL, CNN',
                'github_link': 'https://github.com/ardoktor/DataSciencePractises/tree/main',
                'order': 10,
                'is_featured': False,
            },
            {
                'title': 'Basic Collaborative Filtering Model',
                'slug': 'basic-collaborative-filtering-model',
                'description': 'A basic collaborative filtering recommendation system using Microsoft recommenders library with MovieLens dataset.',
                'year': '2021',
                'tech_stack': 'Python, NumPy, Sklearn',
                'github_link': 'https://github.com/ardoktor/RecommenderSystems/blob/main/huaweiReccomenderv3.ipynb',
                'order': 11,
                'is_featured': False,
            },
        ]

        for p_data in projects:
            Project.objects.get_or_create(
                slug=p_data['slug'],
                defaults=p_data
            )
            self.stdout.write(f'  Created: {p_data["title"]}')

        self.stdout.write(self.style.SUCCESS(f'Done! {Project.objects.count()} projects loaded.'))
