import requests
from django.core.management.base import BaseCommand
from portfolio.models import Project
from datetime import datetime

class Command(BaseCommand):
    help = 'Fetches public repositories from GitHub and populates the Project model'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='GitHub username')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        url = f'https://api.github.com/users/{username}/repos'
        
        self.stdout.write(f'Fetching repos for {username}...')
        
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Failed to fetch repos: {response.status_code}'))
            return

        repos = response.json()
        
        for repo in repos:
            # Skip forks if desired, or keep them. Let's keep them for now.
            
            title = repo['name'].replace('-', ' ').replace('_', ' ').title()
            description = repo['description'] or "No description provided."
            repo_link = repo['html_url']
            live_link = repo['homepage'] or ""
            tech_stack = repo['language'] or "Various"
            
            # Parse date
            created_at_str = repo['created_at']
            created_at = datetime.strptime(created_at_str, '%Y-%m-%dT%H:%M:%SZ').date()

            project, created = Project.objects.get_or_create(
                title=title,
                defaults={
                    'description': description,
                    'repo_link': repo_link,
                    'live_link': live_link,
                    'tech_stack': tech_stack,
                    'created_at': created_at
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created project: {title}'))
            else:
                self.stdout.write(f'Project already exists: {title}')

        self.stdout.write(self.style.SUCCESS('GitHub import completed!'))
