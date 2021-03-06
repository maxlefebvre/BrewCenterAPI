from django.db import models


class CountryCode(models.Model):
    """Defines a country by it's 2 or 3 letter code."""

    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code
