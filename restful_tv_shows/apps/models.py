from django.db import models
import re


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Blog description should be at least 10 characters"
        if len(postData['description']) < 10:
            errors["description"] = "Blog description should be at least 10 characters"
        return errors

    


# Create your models here.
class Show(models.Model):
    title = models.CharField(default="Title*", max_length=255)
    network = models.CharField(default="Network*", max_length=255)
    release_date = models.DateField(null=True)
    description = models.TextField(default="Description*")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    # def __repr__(self):
    #     return f"Show ID: ({self.id})| Title: {self.title}| Network: {self.network}| Release Date: {self.release_date}| Description: {self.description} ||"
    
    def __str__(self):
        return f"{self.id} {self.title} {self.network} {self.release_date} {self.description}"