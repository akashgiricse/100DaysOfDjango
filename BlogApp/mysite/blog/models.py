# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
	STATUS_CHOICES=(
		('draft', 'Draft'),
		('published', 'Published'),

	)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='published')
	author = models.ForeignKey(User, related_name = 'blog_post')
	body = models.TextField()
	publish models.DataTimeField(default = timezone.now)
	created = models.DataTimeField(auto_now_add=True)
	updated = models.DataTimeField(auto_now = True)
	status = modelsl.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	class Meta:
		ordering = ('-publish',)
	def __str__(self):
		return self.title