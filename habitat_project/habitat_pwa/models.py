from django.db import models


class ArtistLineup(models.Model):
    DAY_OF_WEEK = [
        (0, "Friday"),
        (1, "Saturday"),
        (2, "Sunday"),
    ]

    TIME_PERIOD = [
        (0, "Morning Day"),
        (1, "Afternoon"),
        (2, "Evening"),
        (3, "Morning Night"),
    ]

    artist_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    start_time = models.TimeField()
    end_time = models.TimeField()
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK)
    time_period = models.IntegerField(choices=TIME_PERIOD)

    def __str__(self):
        return self.artist_name