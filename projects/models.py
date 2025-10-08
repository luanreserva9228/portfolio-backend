from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=255, help_text="Separe as tags por vírgula. Ex: React,Node.js,PostgreSQL")
    link_github = models.URLField(max_length=200)
    link_demo = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title