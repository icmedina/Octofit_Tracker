from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username="testuser", email="testuser@example.com", password="password123"
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")

class TeamTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username="teamuser", email="teamuser@example.com", password="password123"
        )
        self.team = Team.objects.create(_id=ObjectId(), name="Test Team")
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, "Test Team")
        self.assertIn(self.user, self.team.members.all())

class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username="activityuser", email="activityuser@example.com", password="password123"
        )
        self.activity = Activity.objects.create(
            _id=ObjectId(), user=self.user, activity_type="Running", duration="01:00:00"
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, "Running")
        self.assertEqual(self.activity.user, self.user)

class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            _id=ObjectId(), username="leaderboarduser", email="leaderboarduser@example.com", password="password123"
        )
        self.leaderboard = Leaderboard.objects.create(
            _id=ObjectId(), user=self.user, score=100
        )

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.score, 100)
        self.assertEqual(self.leaderboard.user, self.user)

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            _id=ObjectId(), name="Test Workout", description="A test workout description"
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.name, "Test Workout")
        self.assertEqual(self.workout.description, "A test workout description")

class UserModelTest(TestCase):
    def test_user_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")

class TeamModelTest(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name="Test Team")
        self.assertEqual(team.name, "Test Team")

class ActivityModelTest(TestCase):
    def test_activity_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration="01:00:00")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_leaderboard_creation(self):
        user = User.objects.create(username="testuser", email="testuser@example.com", password="password123")
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(leaderboard.score, 100)

class WorkoutModelTest(TestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name="Test Workout", description="Test Description")
        self.assertEqual(workout.name, "Test Workout")