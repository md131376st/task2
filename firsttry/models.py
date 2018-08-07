from django.db import models


class QueryAnswer(models.Model):
    RID = models.IntegerField()
    RTOE = models.TimeField()

    def __str__(self):
        return str(self.RID)

# Create your models here.
