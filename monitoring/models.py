from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password


class User(models.Model):
    name = models.CharField(max_length=255)
    signup = models.DateField(auto_now_add=True)
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=4, decimal_places=1)

    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z][a-zA-Z0-9_]*$',
                message='The username must start with a letter and contain only letters, numbers or underscores.'
            )
        ]
    )
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        if not self.username:
            last_user = User.objects.order_by('-id').first()
            next_id   = last_user.id + 1 if last_user else 1

            self.username = f'username{next_id}'

        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Workout(models.Model):
    date = models.DateField()
    minutes  = models.PositiveIntegerField()
    nickname = models.CharField(max_length=20, blank=True)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.DecimalField(max_digits=5, decimal_places=1)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.nickname:
            self.nickname = f'workout{self.date}'

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname


class Content(models.Model):
    name  = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    is_movie = models.BooleanField(default=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({'Movie' if self.is_movie else 'Series'})"
