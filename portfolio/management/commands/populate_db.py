from django.core.management.base import BaseCommand
from portfolio.models import Profile, Skill, Project, Experience, Education, Certification
from datetime import date

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **kwargs):
        # Clear existing data to avoid duplicates
        self.stdout.write('Cleaning old data...')
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()

        # Profile
        Profile.objects.create(
            name="Alauddin Taha Faya",
            bio="Versatile and detail-oriented Software Engineer with solid experience in backend development, system architecture, and distributed computing. Proficient in building scalable, high-performance applications using Python and Django.",
            email="alauddinfaya@gmail.com",
            github_link="https://alaauddin.github.io/",
            linkedin_link="https://linkedin.com/in/alauddin-taha-faya-37378019a",
            # resume field would need a file, skipping for now or user uploads later
        )
        self.stdout.write(self.style.SUCCESS('Created Profile'))

        # Skills
        skills_data = [
            ("Python", 95, "fab fa-python"),
            ("Django", 95, "fas fa-code"),
            ("Git & GitHub", 90, "fab fa-git-alt"),
            ("SQL", 85, "fas fa-database"),
            ("Agile Development", 85, "fas fa-users-cog"),
            ("Parallel Programming", 80, "fas fa-network-wired"),
            ("Distributed Computing", 80, "fas fa-server"),
            ("Celery", 85, "fas fa-carrot"), # Using carrot as placeholder or finding better icon
            ("Docker", 80, "fab fa-docker"),
            ("Image Processing", 75, "fas fa-image"),
            ("System Architecture", 85, "fas fa-sitemap"),
        ]
        for name, prof, icon in skills_data:
            Skill.objects.create(name=name, proficiency=prof, icon_class=icon)
        self.stdout.write(self.style.SUCCESS('Created Skills'))

        # Experience
        experiences = [
            {
                "role": "Software Engineer (Django)",
                "company": "FinTechSys",
                "start_date": date(2025, 3, 1),
                "is_current": True,
                "description": "Working on large-scale, AI-driven KYC systems, integrating AI utilities via APIs. Building high-performance, scalable distributed architecture supporting dynamic business logic via DMN models. Implemented pluggable authentication and comprehensive logging.",
                "icon_class": "fas fa-laptop-code"
            },
            {
                "role": "Programming & Systems Officer",
                "company": "Club Sportainment",
                "start_date": date(2024, 3, 1),
                "end_date": date(2025, 3, 1),
                "is_current": False,
                "description": "Established the Programming Dept. Automated customer experiences (Smart gate, Online booking, Maintenance platform).",
                "icon_class": "fas fa-building"
            },
            {
                "role": "Django Developer",
                "company": "PeakByte",
                "start_date": date(2022, 6, 1),
                "is_current": True,
                "description": "Django Development.",
                "icon_class": "fab fa-python"
            },
            {
                "role": "Software Architect Trainee",
                "company": "Tharwat",
                "start_date": date(2023, 11, 1),
                "end_date": date(2024, 1, 31),
                "is_current": False,
                "description": "Comprehensive training in Business Modeling, OOP, SOLID, Design Patterns, Clean Architecture, API Dev, Unit Testing, Agile/Scrum, Azure DevOps.",
                "icon_class": "fas fa-drafting-compass"
            },
            {
                "role": "Django Developer Trainee",
                "company": "NCBC",
                "start_date": date(2023, 8, 1),
                "end_date": date(2023, 9, 30),
                "is_current": False,
                "description": "National Center in Big Data and Cloud Computing training.",
                "icon_class": "fas fa-cloud"
            },
            {
                "role": "FYP Project Lead",
                "company": "NCL - NED",
                "start_date": date(2022, 2, 1),
                "end_date": date(2023, 8, 31),
                "is_current": False,
                "description": "Energy Efficient AI Core on FPGA for Point of Care Application (Diabetic Retinopathy).",
                "icon_class": "fas fa-microchip"
            },
             {
                "role": "AI Trainee",
                "company": "NCL - NED",
                "start_date": date(2023, 1, 1),
                "end_date": date(2023, 3, 31),
                "is_current": False,
                "description": "Artificial Intelligence training.",
                "icon_class": "fas fa-brain"
            },
            {
                "role": "Customer Service Specialist",
                "company": "Snoonu",
                "start_date": date(2021, 9, 1),
                "end_date": date(2021, 11, 30),
                "is_current": False,
                "description": "Customer service operations.",
                "icon_class": "fas fa-headset"
            }
        ]
        
        for exp in experiences:
            Experience.objects.create(**exp)
        self.stdout.write(self.style.SUCCESS('Created Experience'))

        # Education
        educations = [
            {
                "degree": "Bachelor's in CIS Security",
                "institution": "NED University",
                "year": "2019 - 2023",
                "icon_class": "fas fa-user-graduate"
            },
            {
                "degree": "High School, Sciences",
                "institution": "Kuwait Secondary School",
                "year": "2014 - 2017",
                "icon_class": "fas fa-school"
            },
            {
                "degree": "Matriculation",
                "institution": "Al-Methaq School",
                "year": "2011 - 2014",
                "icon_class": "fas fa-book"
            }
        ]
        for edu in educations:
            Education.objects.create(**edu)
        self.stdout.write(self.style.SUCCESS('Created Education'))

        # Certifications
        certs = [
            ("AWS Certified Solutions Architect", "Amazon Web Services", date(2023, 5, 15), "fab fa-aws"), # Date estimated based on context or generic
            ("Professional Scrum Master I", "Scrum.org", date(2022, 11, 20), "fas fa-certificate"),
            ("Building Web Applications in Django", "University of Michigan", date(2023, 1, 1), "fab fa-python"),
            ("Introduction to Databases", "Meta", date(2023, 1, 1), "fas fa-database"),
            ("Programming with JavaScript", "Meta", date(2023, 1, 1), "fab fa-js"),
            ("Introduction to Agile Development and Scrum", "IBM", date(2023, 1, 1), "fas fa-tasks"),
            ("Data Visualization", "Kaggle", date(2023, 1, 1), "fas fa-chart-bar"),
            ("Introduction to Git and GitHub", "Google", date(2023, 1, 1), "fab fa-github"),
            ("Python (Basics)", "HackerRank", date(2023, 1, 1), "fab fa-python"),
            ("Problem Solving", "HackerRank", date(2023, 1, 1), "fas fa-puzzle-piece"),
        ]
        
        for name, issuer, d, icon in certs:
            Certification.objects.create(
                name=name,
                issuer=issuer,
                date=d,
                icon_class=icon
            )
        self.stdout.write(self.style.SUCCESS('Created Certifications'))

        self.stdout.write(self.style.SUCCESS('Database populated successfully with CV data!'))
