from django.db import models
import uuid


class UserProfileModel(models.Model):

    class Meta:
        db_table = 'UserProfiles'

    # no choice/text fill
    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30)

    # single choice
    location = models.CharField(max_length=40, null=False)
    hackathons = models.IntegerField(null=False)

    # multiple choice
    progLanguages = models.TextField(null=False)
    databases = models.TextField(null=False)
    interests = models.TextField(null=False)
    latest = models.BooleanField(default=1, null=False)

    def __str__(self):
        return self.username
