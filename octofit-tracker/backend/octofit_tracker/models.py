from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list)  # Set default to an empty list

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Simplified for testing
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.activity_type} by {self.user.username}"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)  # Simplified for testing
    score = models.IntegerField()

    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name