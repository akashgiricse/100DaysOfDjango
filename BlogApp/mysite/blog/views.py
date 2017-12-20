# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
	object_list = Post.published.all()
	paginator = Paginator(object_list, 3) # 3 post in each page
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# if page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)
	
	return render(request, 'blog/post/list.html',{'page':page, 'posts':posts})

def post_detail(request,year,month, day, post):
	post = get_object_or_404(Post,slug=post, 
		status='published',
		publish__year=year, 
		publish__month=month,
		publish__day = day
		)
	return render(request, 'blog/post/detail.html',
		{'post':post})

class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'post'
	paginate_by = 3
	template_name = 'blog/post/list.html'