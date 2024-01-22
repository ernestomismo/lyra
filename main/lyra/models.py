import datetime
from django.db import models
from django.utils import timezone

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

class Tag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag_text = models.CharField(max_length=100)
    def __str__(self):
        return self.tag_text
    
class Document(models.Model):
    BOOK = "BO"
    ARTICLE = "AR"
    CHAPTER = " CH"
    TEXT_DOC = "TX"
    SLIDES = "SL"
    TYPE_OF_DOC = [(BOOK, "Book"), (ARTICLE, "Article"), (CHAPTER, "Chapter"), (TEXT_DOC, "Texto"),
                   (SLIDES, "Slides")]
    project = models.ManyToManyField(Project)
    document_name = models.CharField(max_length=200)
    description = models.TextField()
    type_of_document = models.CharField(max_length=40, choices=TYPE_OF_DOC)
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.tag_text