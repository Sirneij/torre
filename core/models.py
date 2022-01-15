from django.db import models


class Person(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=30)
    name = models.CharField("Person's name", max_length=300)
    professional_headline = models.CharField("Professional Headline", max_length=300, blank=True)
    picture = models.URLField("Link to picture", max_length=2000, blank=True)
    bio = models.TextField("Biographical summary", blank=True)
    username = models.CharField("Username", max_length=50, blank=True)
    skills = models.JSONField("Skill", default=dict)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return self.name
