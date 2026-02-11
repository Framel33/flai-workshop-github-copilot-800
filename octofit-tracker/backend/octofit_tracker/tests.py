from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    """Test cases for User model"""

    def setUp(self):
        self.user = User.objects.create(
            name='Test Hero',
            email='test@example.com',
            password='test_password',
            team='Test Team'
        )

    def test_user_creation(self):
        """Test user is created successfully"""
        self.assertEqual(self.user.name, 'Test Hero')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.team, 'Test Team')

    def test_user_str(self):
        """Test user string representation"""
        self.assertEqual(str(self.user), 'Test Hero')


class TeamModelTest(TestCase):
    """Test cases for Team model"""

    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team',
            members=['test1@example.com', 'test2@example.com']
        )

    def test_team_creation(self):
        """Test team is created successfully"""
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(len(self.team.members), 2)

    def test_team_str(self):
        """Test team string representation"""
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    """Test cases for Activity model"""

    def setUp(self):
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=250,
            date=timezone.now()
        )

    def test_activity_creation(self):
        """Test activity is created successfully"""
        self.assertEqual(self.activity.user_email, 'test@example.com')
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)


class UserAPITest(APITestCase):
    """Test cases for User API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            name='API Test Hero',
            email='api@example.com',
            password='api_password',
            team='API Team'
        )

    def test_get_users(self):
        """Test retrieving list of users"""
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_detail(self):
        """Test retrieving a single user"""
        response = self.client.get(f'/users/{self.user._id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'API Test Hero')

    def test_create_user(self):
        """Test creating a new user"""
        data = {
            'name': 'New Hero',
            'email': 'new@example.com',
            'password': 'new_password',
            'team': 'New Team'
        }
        response = self.client.post('/users/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITest(APITestCase):
    """Test cases for Team API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(
            name='API Test Team',
            description='Test team for API',
            members=['test1@example.com']
        )

    def test_get_teams(self):
        """Test retrieving list of teams"""
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_team(self):
        """Test creating a new team"""
        data = {
            'name': 'New Team',
            'description': 'A new test team',
            'members': []
        }
        response = self.client.post('/teams/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ActivityAPITest(APITestCase):
    """Test cases for Activity API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.activity = Activity.objects.create(
            user_email='test@example.com',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=250,
            date=timezone.now()
        )

    def test_get_activities(self):
        """Test retrieving list of activities"""
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_activities_by_user(self):
        """Test filtering activities by user email"""
        response = self.client.get('/activities/by_user/?email=test@example.com')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class LeaderboardAPITest(APITestCase):
    """Test cases for Leaderboard API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.entry = Leaderboard.objects.create(
            user_email='test@example.com',
            user_name='Test Hero',
            team='Test Team',
            total_calories=1000,
            total_activities=10,
            total_duration=300,
            rank=1
        )

    def test_get_leaderboard(self):
        """Test retrieving leaderboard"""
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_top_leaderboard(self):
        """Test retrieving top N entries"""
        response = self.client.get('/leaderboard/top/?limit=5')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WorkoutAPITest(APITestCase):
    """Test cases for Workout API endpoints"""

    def setUp(self):
        self.client = APIClient()
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout routine',
            activity_type='Running',
            duration=30,
            difficulty='Intermediate',
            calories_estimate=300
        )

    def test_get_workouts(self):
        """Test retrieving list of workouts"""
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_workouts_by_difficulty(self):
        """Test filtering workouts by difficulty"""
        response = self.client.get('/workouts/by_difficulty/?difficulty=Intermediate')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
