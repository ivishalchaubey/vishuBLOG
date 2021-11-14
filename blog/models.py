from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class blogPostModel(models.Model):
    blog_title = models.CharField(max_length=200)
    blog_time = models.DateTimeField(auto_now_add=True)
    blog_image = models.ImageField(upload_to="blog/",max_length=259)
    blog_desc = HTMLField()
    blog_slug = AutoSlugField(populate_from= "blog_title",unique=True)
    
class useremail(models.Model):
    emails = models.EmailField()
    
    def __str__(self):
        return self.emails