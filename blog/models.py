from django.db import models


class Blog(models.Model):
    blog_title = models.TextField(max_length=200)
    blog_content = models.TextField()
    blog_date = models.DateTimeField('date published')

    def __str__(self):
        return self.blog_title
    

class Projects(models.Model):
    name = models.CharField(max_length=200)
    startDate = models.DateField()
    endDate = models.DateField()
    description = models.TextField()
    highlights = models.CharField(max_length=400, null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name