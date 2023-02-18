from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_date = models.DateTimeField(null=False, auto_now_add=True)
    updated_date = models.DateTimeField(null=False, auto_now=True)
    active = models.BooleanField(null=False)


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Course(BaseModel):
    subject = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.subject
