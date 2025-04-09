from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data using the database API to avoid issues with unhashable model instances
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM octofit_tracker_user")
            cursor.execute("DELETE FROM octofit_tracker_team")
            cursor.execute("DELETE FROM octofit_tracker_activity")
            cursor.execute("DELETE FROM octofit_tracker_leaderboard")
            cursor.execute("DELETE FROM octofit_tracker_workout")

        # Ensure that the `_id` field is not explicitly set to `null` or left uninitialized
        # Create users
        users = []
        user_data = [
            {'username': 'thundergod', 'email': 'thundergod@mhigh.edu', 'password': 'password123'},
            {'username': 'metalgeek', 'email': 'metalgeek@mhigh.edu', 'password': 'password123'},
            {'username': 'zerocool', 'email': 'zerocool@mhigh.edu', 'password': 'password123'},
            {'username': 'crashoverride', 'email': 'crashoverride@mhigh.edu', 'password': 'password123'},
            {'username': 'sleeptoken', 'email': 'sleeptoken@mhigh.edu', 'password': 'password123'},
        ]
        for data in user_data:
            user = User(**data)
            user.save()
            users.append(user)

        # Create teams
        team1 = Team(_id=ObjectId(), name='Blue Team')
        team2 = Team(_id=ObjectId(), name='Gold Team')
        team1.save()
        team2.save()

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0], activity_type='Cycling', duration=timedelta(hours=1)),
            Activity(_id=ObjectId(), user=users[1], activity_type='Crossfit', duration=timedelta(hours=2)),
            Activity(_id=ObjectId(), user=users[2], activity_type='Running', duration=timedelta(hours=1, minutes=30)),
            Activity(_id=ObjectId(), user=users[3], activity_type='Strength', duration=timedelta(minutes=30)),
            Activity(_id=ObjectId(), user=users[4], activity_type='Swimming', duration=timedelta(hours=1, minutes=15)),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
