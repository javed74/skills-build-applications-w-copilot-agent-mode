# This file contains test data for the OctoFit Tracker application.

def get_test_users():
    return [
        {
            "username": "testuser1",
            "email": "testuser1@example.com",
            "password": "password123",
        },
        {
            "username": "testuser2",
            "email": "testuser2@example.com",
            "password": "password456",
        },
    ]

def get_test_workouts():
    return [
        {
            "name": "Morning Run",
            "duration": 30,
            "calories_burned": 300,
        },
        {
            "name": "Evening Yoga",
            "duration": 45,
            "calories_burned": 200,
        },
    ]
