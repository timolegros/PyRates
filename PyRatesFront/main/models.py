from django.db import models
import uuid


class UserProfileModel(models.Model):

    class Meta:
        db_table = 'UserProfiles'

    userID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30)

    progLanguageChoices = (('1', 'C'), ('2', 'Python'), ('3', 'Javascript'), ('4', 'Java'), ('5', 'C#'), ('6', 'C++'))
    databaseChoices = (('1', 'SQL'), ('2', 'MongoDB'), ('3', 'Firebase'), ('4', 'Oracle'), ('5', 'Redis'))
    locationChoices = (('1', "East Coast"), ('2', "Midwest"), ('3', "West Coast"), ('4', "Southern US"),
                       ('5', "Northern US"), ('6', "Eastern Canada"), ('7', "Western Canada"),
                       ('8', "Atlantic Provinces"), ('9', "Outside US/ Canada"))
    areaOfInterestChoices = (('1', "Web Development"), ('2', "AI"), ('3', "Product Management"), ('4', "Big data"))

    progChoice = models.CharField('Programming language', max_length=20, choices=progLanguageChoices)
    dbChoice = models.CharField('Databases', max_length=20, choices=databaseChoices)
    locChoice = models.CharField('Location', max_length=20, choices=locationChoices)
    interestChoice = models.CharField('Area of interest', max_length=20, choices=areaOfInterestChoices)

    def __str__(self):
        return self.username
