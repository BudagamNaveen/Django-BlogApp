from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class BlogData(models.Model):
	Title = models.CharField(max_length=200)
	Description = models.TextField()
	Image = models.ImageField(default='default.jpg',upload_to='blog_pics/')
	Hashtag = models.CharField(max_length=200)

	def __str__(self):
		return self.Title

	def get_absolute_url(self):
		return reverse("BlogView")

class CommentSection(models.Model):
	Comment  = models.TextField()

	def __str__(self):
		return self.Comment

class NewBlogData(models.Model):
	Newusername = models.ForeignKey(User,on_delete=models.CASCADE,default=26)
	NewTitle = models.CharField(max_length=200)
	NewDescription = models.TextField()
	NewImage = models.ImageField(default='default.jpg',upload_to='blog_pics/')
	NewHashtag = models.CharField(max_length=200)

	def __str__(self):
		return self.NewTitle

	def get_absolute_url(self):
		return reverse("BlogView")
