from rest_framework.test import APITestCase
from rest_framework import status
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        data = {"username": "testuser", "email": "testuser@example.com", "password": "password123"}
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_users(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TeamTests(APITestCase):
    def test_create_team(self):
        data = {"name": "Team A"}
        response = self.client.post("/teams/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_teams(self):
        response = self.client.get("/teams/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        data = {"name": "Running", "calories_burned": 300}
        response = self.client.post("/activities/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_activities(self):
        response = self.client.get("/activities/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class LeaderboardTests(APITestCase):
    def test_get_leaderboard(self):
        response = self.client.get("/leaderboard/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        data = {"name": "Morning Workout", "duration": 60}
        response = self.client.post("/workouts/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_workouts(self):
        response = self.client.get("/workouts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
