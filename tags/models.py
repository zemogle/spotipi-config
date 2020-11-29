from django.db import models

SOURCES = ((1,'spotify'),)

class Tag(models.Model):
    name = models.TextField('Song or playlist name')
    tagid = models.CharField(max_length=50)
    volume = models.FloatField()
    uri = models.TextField()
    source = models.SmallIntegerField(choices=SOURCES)

    def __str__(self):
        return f"{self.name} - {self.tagid}"
