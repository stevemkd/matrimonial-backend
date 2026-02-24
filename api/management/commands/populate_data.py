from django.core.management.base import BaseCommand
from api.models import Profile
import random

class Command(BaseCommand):
    help = 'Populate the database with sample matrimonial profiles'

    def handle(self, *args, **options):
        # Clear existing profiles
        Profile.objects.all().delete()
        
        sample_profiles = [
            {
                'full_name': 'Priya Menon',
                'gender': 'F',
                'age': 28,
                'height': '5\'4"',
                'education': 'MBA',
                'profession': 'Software Engineer',
                'location': 'Kochi, Kerala',
                'religion': 'Hindu',
                'caste': 'Nair',
                'image_url': 'https://i.pravatar.cc/300?img=1',
                'verified': True,
                'premium': True,
                'bio': 'Looking for a life partner who values family, tradition, and growth.',
                'interests': ['Reading', 'Travel', 'Music', 'Cooking'],
            },
            {
                'full_name': 'Anjali Nair',
                'gender': 'F',
                'age': 26,
                'height': '5\'2"',
                'education': 'B.Tech',
                'profession': 'Doctor',
                'location': 'Thiruvananthapuram, Kerala',
                'religion': 'Hindu',
                'caste': 'Nair',
                'image_url': 'https://i.pravatar.cc/300?img=2',
                'verified': True,
                'premium': False,
                'bio': 'Doctor by profession, passionate about helping others.',
                'interests': ['Medicine', 'Yoga', 'Dancing'],
            },
            {
                'full_name': 'Sneha Pillai',
                'gender': 'F',
                'age': 27,
                'height': '5\'5"',
                'education': 'M.Sc',
                'profession': 'Teacher',
                'location': 'Kozhikode, Kerala',
                'religion': 'Hindu',
                'caste': 'Nair',
                'image_url': 'https://i.pravatar.cc/300?img=3',
                'verified': False,
                'premium': True,
                'bio': 'Educator who loves teaching and learning new things.',
                'interests': ['Teaching', 'Reading', 'Art'],
            },
            {
                'full_name': 'Meera Iyer',
                'gender': 'F',
                'age': 29,
                'height': '5\'3"',
                'education': 'CA',
                'profession': 'Chartered Accountant',
                'location': 'Thrissur, Kerala',
                'religion': 'Hindu',
                'caste': 'Iyer',
                'image_url': 'https://i.pravatar.cc/300?img=4',
                'verified': True,
                'premium': True,
                'bio': 'Finance professional seeking a compatible partner.',
                'interests': ['Finance', 'Travel', 'Photography'],
            },
            {
                'full_name': 'Divya Menon',
                'gender': 'F',
                'age': 25,
                'height': '5\'1"',
                'education': 'B.Com',
                'profession': 'Business Analyst',
                'location': 'Kannur, Kerala',
                'religion': 'Hindu',
                'caste': 'Nair',
                'image_url': 'https://i.pravatar.cc/300?img=5',
                'verified': True,
                'premium': False,
                'bio': 'Analytical mind with a creative heart.',
                'interests': ['Business', 'Music', 'Dancing'],
            },
            {
                'full_name': 'Riya Nair',
                'gender': 'F',
                'age': 30,
                'height': '5\'6"',
                'education': 'M.Phil',
                'profession': 'Research Scholar',
                'location': 'Kottayam, Kerala',
                'religion': 'Hindu',
                'caste': 'Nair',
                'image_url': 'https://i.pravatar.cc/300?img=6',
                'verified': True,
                'premium': True,
                'bio': 'Passionate researcher and academic.',
                'interests': ['Research', 'Writing', 'Classical Music'],
            },
            {
                'full_name': 'Arjun Kumar',
                'gender': 'M',
                'age': 32,
                'height': '5\'10"',
                'education': 'M.Tech',
                'profession': 'IT Manager',
                'location': 'Bangalore, Karnataka',
                'religion': 'Hindu',
                'caste': 'Brahmin',
                'image_url': 'https://i.pravatar.cc/300?img=7',
                'verified': True,
                'premium': True,
                'bio': 'Tech professional looking for a life partner.',
                'interests': ['Technology', 'Gaming', 'Travel'],
            },
            {
                'full_name': 'Rahul Sharma',
                'gender': 'M',
                'age': 29,
                'height': '5\'11"',
                'education': 'MBA',
                'profession': 'Marketing Manager',
                'location': 'Mumbai, Maharashtra',
                'religion': 'Hindu',
                'caste': 'Sharma',
                'image_url': 'https://i.pravatar.cc/300?img=8',
                'verified': False,
                'premium': False,
                'bio': 'Marketing professional with a passion for life.',
                'interests': ['Marketing', 'Sports', 'Movies'],
            },
        ]

        created_profiles = []
        for profile_data in sample_profiles:
            profile = Profile.objects.create(**profile_data)
            created_profiles.append(profile)
            self.stdout.write(
                self.style.SUCCESS(f'Created profile: {profile.full_name}')
            )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(created_profiles)} profiles')
        )
