import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser


class UUidModelMixin(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4(), editable=False)

    class Meta:
        abstract = True


class CustomUser(AbstractUser, UUidModelMixin):
    pass

    def __str__(self):
        return self.username


class Ads(models.Model):
    pass


class Animals(models.Model):
    pass
