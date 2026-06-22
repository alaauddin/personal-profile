from django.test import TestCase
from django.urls import reverse
from datetime import date
from .models import Profile, Experience

class ExperienceOrderingTest(TestCase):
    def setUp(self):
        # Create a basic profile since the home view retrieves it
        self.profile = Profile.objects.create(
            name="Test User",
            bio="Test Bio",
            email="test@example.com"
        )
        
        # Create some experience objects with varying start dates and current status
        # Exp 1: Old current job, started 2020
        self.exp1 = Experience.objects.create(
            role="Old Current Developer",
            company="Company A",
            start_date=date(2020, 1, 1),
            is_current=True,
            description="Did some dev work"
        )
        
        # Exp 2: Newer past job, started 2021
        self.exp2 = Experience.objects.create(
            role="Newer Past Developer",
            company="Company B",
            start_date=date(2021, 2, 1),
            end_date=date(2022, 1, 1),
            is_current=False,
            description="Currently devving"
        )
        
        # Exp 3: Old past job, started 2018
        self.exp3 = Experience.objects.create(
            role="Junior Developer",
            company="Company C",
            start_date=date(2018, 1, 1),
            end_date=date(2019, 12, 31),
            is_current=False,
            description="Began devving"
        )
        
        # Exp 4: Newest current job, started 2022
        self.exp4 = Experience.objects.create(
            role="Newest Current Developer",
            company="Company D",
            start_date=date(2022, 1, 1),
            is_current=True,
            description="Currently leading"
        )

    def test_experience_ordering(self):
        """
        Verify that experiences are ordered such that 'is_current=True' (Present)
        is placed first, ordered by start_date descending, followed by non-current
        experiences ordered by start_date descending.
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        
        experiences = list(response.context['experiences'])
        
        # Expected order:
        # 1. exp4 (is_current=True, start_date=2022-01-01)
        # 2. exp1 (is_current=True, start_date=2020-01-01)
        # 3. exp2 (is_current=False, start_date=2021-02-01)
        # 4. exp3 (is_current=False, start_date=2018-01-01)
        expected_order = [self.exp4, self.exp1, self.exp2, self.exp3]
        
        self.assertEqual(experiences, expected_order)
