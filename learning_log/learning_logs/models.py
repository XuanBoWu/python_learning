from django.db import models

# Create your models here.

class Topic(models.Model):
    """ User's learning topic """

    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        """ Return the string representation of the model """
        return self.text

class Entry(models.Model):
    """ specific knowledge acquired about a particular topic. """
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self) -> str:
        
        if len(self.text) <= 50:
            return f"{self.text}"
        else:
            return f"{self.text[:50]}..."
        