from django.db import models

# Create your models here.


class Todo(models.Model):
    userId = models.PositiveIntegerField(primary_key=True)
    todoId = models.PositiveIntegerField()
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = "todo"


class Users(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    website = models.CharField(max_length=30)

    class Meta:
        db_table = "users"

# TODO Create dependent tables Address and Company for Users
