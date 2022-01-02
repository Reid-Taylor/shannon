from django.db import models
from django.utils import timezone

# Create your models here.
class Gene(models.Model):
    gene = models.CharField(max_length=100)
    identifier = models.IntegerField()
    assignee = models.CharField(max_length=100)
    finished = models.BooleanField(default=0)
    def __str__(self):
        """Returns a string representation of a message."""
        return f"Specimen {self.gene} - DMDD{self.identifier} is {'' if self.finished else 'not'} finished.\nThis assignment belongs to {self.assignee}.\n"

class PictureInfo(models.Model):
    gene = models.CharField(max_length=100)
    identifier = models.IntegerField()
    slide = models.IntegerField()
    imgsrc = models.CharField(max_length=600)
    mutated = models.BooleanField("mutation present")
    comment = models.CharField(max_length=450)
    submission = models.DateTimeField("date logged")
    author = models.CharField(max_length=150)
    wildtype = models.BooleanField("wildtype")
    center = models.CharField(
        max_length=32,
        choices=(
        ('0750', '750'),
        ('0775', '775'),
        ('0800', '800'),
        ('0825', '825'),
        ('0850', '850'),
        ('0875', '875'),
        ('0900', '900'),
        ('0925', '925'),
        ('0950', '950'),
        ),
        null=True
    )
    leftPresent = models.BooleanField("left gland beginning present")
    leftBeginning = models.CharField(
        max_length=32,
        choices=(
        ('0750', '750'),
        ('0775', '775'),
        ('0800', '800'),
        ('0825', '825'),
        ('0850', '850'),
        ('0875', '875'),
        ('0900', '900'),
        ('0925', '925'),
        ('0950', '950'),
        ),
        null=True
    )
    rightPresent = models.BooleanField("right gland beginning present")
    rightBeginning = models.CharField(
        max_length=32,
        choices=(
        ('0750', '750'),
        ('0775', '775'),
        ('0800', '800'),
        ('0825', '825'),
        ('0850', '850'),
        ('0875', '875'),
        ('0900', '900'),
        ('0925', '925'),
        ('0950', '950'),
        ),
        null=True
    )

    def __str__(self):
        """Returns a string representation of a message."""
        return f"Specimen {self.gene} - DMDD{self.identifier} located at '{self.imgsrc}' was marked for mutation presence as '{self.mutated}' by '{self.author}' on {self.submission.strftime('%A, %d %B, %Y at %X')} \n Additionally, the pituitary ranges from {self.leftBeginning} to {self.rightBeginning}"