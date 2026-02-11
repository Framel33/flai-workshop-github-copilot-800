from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database population...'))

        # Clear existing data
        self.stdout.write('Clearing existing data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes united for fitness!',
            members=[]
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League training for peak performance!',
            members=[]
        )

        # Create Marvel Users
        self.stdout.write('Creating Marvel heroes...')
        marvel_users = [
            User.objects.create(
                name='Iron Man',
                email='ironman@marvel.com',
                password='arc_reactor_3000',
                team='Team Marvel'
            ),
            User.objects.create(
                name='Captain America',
                email='cap@marvel.com',
                password='shield_bearer',
                team='Team Marvel'
            ),
            User.objects.create(
                name='Thor',
                email='thor@marvel.com',
                password='mjolnir_worthy',
                team='Team Marvel'
            ),
            User.objects.create(
                name='Black Widow',
                email='blackwidow@marvel.com',
                password='red_room_elite',
                team='Team Marvel'
            ),
            User.objects.create(
                name='Hulk',
                email='hulk@marvel.com',
                password='smash_time',
                team='Team Marvel'
            ),
        ]

        # Create DC Users
        self.stdout.write('Creating DC heroes...')
        dc_users = [
            User.objects.create(
                name='Superman',
                email='superman@dc.com',
                password='krypton_son',
                team='Team DC'
            ),
            User.objects.create(
                name='Batman',
                email='batman@dc.com',
                password='dark_knight',
                team='Team DC'
            ),
            User.objects.create(
                name='Wonder Woman',
                email='wonderwoman@dc.com',
                password='amazon_warrior',
                team='Team DC'
            ),
            User.objects.create(
                name='Flash',
                email='flash@dc.com',
                password='speed_force',
                team='Team DC'
            ),
            User.objects.create(
                name='Aquaman',
                email='aquaman@dc.com',
                password='atlantis_king',
                team='Team DC'
            ),
        ]

        # Update team members
        team_marvel.members = [user.email for user in marvel_users]
        team_marvel.save()
        team_dc.members = [user.email for user in dc_users]
        team_dc.save()

        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        all_users = marvel_users + dc_users

        for i, user in enumerate(all_users):
            for day in range(7):
                activity_date = timezone.now() - timedelta(days=day)
                activity_type = activity_types[(i + day) % len(activity_types)]
                
                Activity.objects.create(
                    user_email=user.email,
                    activity_type=activity_type,
                    duration=30 + (i * 5) + (day * 2),
                    distance=5.0 + (i * 0.5) + (day * 0.3) if activity_type in ['Running', 'Cycling', 'Swimming'] else None,
                    calories=200 + (i * 20) + (day * 10),
                    date=activity_date
                )

        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard...')
        for rank, user in enumerate(all_users, start=1):
            user_activities = Activity.objects.filter(user_email=user.email)
            total_calories = sum(activity.calories for activity in user_activities)
            total_duration = sum(activity.duration for activity in user_activities)
            
            Leaderboard.objects.create(
                user_email=user.email,
                user_name=user.name,
                team=user.team,
                total_calories=total_calories,
                total_activities=user_activities.count(),
                total_duration=total_duration,
                rank=rank
            )

        # Create Workouts
        self.stdout.write('Creating workout suggestions...')
        workouts = [
            {
                'name': 'Super Soldier Strength',
                'description': 'Captain America\'s legendary strength training routine',
                'activity_type': 'Weightlifting',
                'duration': 60,
                'difficulty': 'Advanced',
                'calories_estimate': 400
            },
            {
                'name': 'Speed Force Sprint',
                'description': 'Flash-inspired high-intensity interval training',
                'activity_type': 'Running',
                'duration': 30,
                'difficulty': 'Intermediate',
                'calories_estimate': 350
            },
            {
                'name': 'Amazonian Warrior Training',
                'description': 'Wonder Woman\'s combat and flexibility routine',
                'activity_type': 'Yoga',
                'duration': 45,
                'difficulty': 'Intermediate',
                'calories_estimate': 250
            },
            {
                'name': 'Asgardian Endurance',
                'description': 'Thor\'s hammer-swinging cardio blast',
                'activity_type': 'Boxing',
                'duration': 50,
                'difficulty': 'Advanced',
                'calories_estimate': 450
            },
            {
                'name': 'Atlantean Aquatics',
                'description': 'Aquaman\'s underwater swimming mastery',
                'activity_type': 'Swimming',
                'duration': 40,
                'difficulty': 'Beginner',
                'calories_estimate': 300
            },
            {
                'name': 'Dark Knight Detective Work',
                'description': 'Batman\'s stealth and agility training',
                'activity_type': 'Cycling',
                'duration': 55,
                'difficulty': 'Advanced',
                'calories_estimate': 380
            },
            {
                'name': 'Widow\'s Flexibility Flow',
                'description': 'Black Widow\'s signature flexibility routine',
                'activity_type': 'Yoga',
                'duration': 35,
                'difficulty': 'Beginner',
                'calories_estimate': 200
            },
            {
                'name': 'Hulk Smash Power',
                'description': 'Unleash your inner strength with power lifting',
                'activity_type': 'Weightlifting',
                'duration': 45,
                'difficulty': 'Advanced',
                'calories_estimate': 420
            },
        ]

        for workout_data in workouts:
            Workout.objects.create(**workout_data)

        # Print summary
        self.stdout.write(self.style.SUCCESS('\n=== Database Population Complete ==='))
        self.stdout.write(f'Teams created: {Team.objects.count()}')
        self.stdout.write(f'Users created: {User.objects.count()}')
        self.stdout.write(f'Activities created: {Activity.objects.count()}')
        self.stdout.write(f'Leaderboard entries: {Leaderboard.objects.count()}')
        self.stdout.write(f'Workouts created: {Workout.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\nDatabase is ready for action! 🦸‍♂️🦸‍♀️'))
