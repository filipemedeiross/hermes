from django.test import TestCase
from django.utils.timezone import now
from django.contrib.auth.hashers import check_password

from datetime   import date
from monitoring.models import User,    \
                              Workout, \
                              Content


class UserModelTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            name='John',
            height=1.75,
            weight=70.5,
            username='john_doe',
            password='password',
        )
        self.user2 = User.objects.create(
            name='Jane',
            height=1.65,
            weight=60.0,
            password='password'
        )

    def test_user_creation(self):
        self.assertEqual(self.user1.name, 'John')
        self.assertEqual(self.user1.signup, now().date())
        self.assertEqual(self.user1.height, 1.75)
        self.assertEqual(self.user1.weight, 70.5)

        self.assertEqual(self.user2.name, 'Jane')
        self.assertEqual(self.user2.signup, now().date())
        self.assertEqual(self.user2.height, 1.65)
        self.assertEqual(self.user2.weight, 60.0)

    def test_password_is_hashed(self):
        self.assertNotEqual(self.user1.password, 'password')
        self.assertTrue(self.user1.password.startswith('pbkdf2_'))
        self.assertTrue(check_password('password', self.user1.password))

        self.assertNotEqual(self.user2.password, 'password')
        self.assertTrue(self.user2.password.startswith('pbkdf2_'))
        self.assertTrue(check_password('password', self.user2.password))

    def test_username_assignment(self):
        self.assertEqual(self.user1.username, 'john_doe')
        self.assertEqual(self.user2.username, f'username{self.user2.id}')

    def test_str_representation(self):
        self.assertEqual(str(self.user1), 'john_doe')
        self.assertEqual(str(self.user2), self.user2.username)


class WorkoutModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Alice',
            height=1.68,
            weight=65.0,
            password='secure_pass'
        )
        self.workout = Workout.objects.create(
            date=date(2024, 2, 20),
            minutes=60,
            distance=5.00,
            calories=400.5,
            user=self.user
        )

    def test_workout_creation(self):
        self.assertEqual(self.workout.minutes ,    60)
        self.assertEqual(self.workout.distance,  5.00)
        self.assertEqual(self.workout.calories, 400.5)
        self.assertEqual(self.workout.user, self.user)

    def test_workout_default_nickname(self):
        self.assertEqual(self.workout.nickname, 'workout2024-02-20')

    def test_str_representation(self):
        self.assertEqual(str(self.workout), 'workout2024-02-20')


class ContentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Bob',
            height=1.80,
            weight=80.0,
            password='another_pass'
        )
        self.content = Content.objects.create(
            name='Inception',
            genre='Sci-Fi',
            platform='Netflix',
            user=self.user
        )

    def test_content_creation(self):
        self.assertEqual(self.content.name  , 'Inception')
        self.assertEqual(self.content.genre ,    'Sci-Fi')
        self.assertEqual(self.content.platform, 'Netflix')
        self.assertEqual(self.content.user, self.user)
        self.assertTrue(self.content.is_movie)

    def test_str_representation(self):
        self.assertEqual(str(self.content), 'Inception (Movie)')

    def test_content_is_series(self):
        self.content.is_movie = False
        self.content.save()
        self.assertEqual(str(self.content), 'Inception (Series)')


class UserWorkoutRelationshipTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Jane',
            height=1.70,
            weight=65.0,
            password='secure_password'
        )
        self.workout1 = Workout.objects.create(
            date=date(2024, 2, 20),
            minutes=45,
            distance=3.50,
            calories=250.5,
            user=self.user
        )
        self.workout2 = Workout.objects.create(
            date=date(2024, 2, 21),
            minutes=60,
            distance=5.00,
            calories=400.0,
            user=self.user
        )

    def test_user_has_multiple_workouts(self):
        workouts = Workout.objects.filter(user=self.user)
        self.assertEqual(workouts.count(),  2)
        self.assertIn(self.workout1, workouts)
        self.assertIn(self.workout2, workouts)

    def test_workouts_belong_to_user(self):
        self.assertEqual(self.workout1.user, self.user)
        self.assertEqual(self.workout2.user, self.user)


class UserContentRelationshipTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Sam',
            height=1.80,
            weight=75.0,
            password='another_password'
        )
        self.content1 = Content.objects.create(
            name='The Matrix',
            genre='Sci-Fi',
            platform='HBO',
            user=self.user
        )
        self.content2 = Content.objects.create(
            name='Breaking Bad',
            genre='Crime',
            platform='Netflix',
            is_movie=False,
            user=self.user
        )

    def test_user_has_multiple_contents(self):
        contents = Content.objects.filter(user=self.user)
        self.assertEqual(contents.count(),  2)
        self.assertIn(self.content1, contents)
        self.assertIn(self.content2, contents)

    def test_content_belongs_to_user(self):
        self.assertEqual(self.content1.user, self.user)
        self.assertEqual(self.content2.user, self.user)
