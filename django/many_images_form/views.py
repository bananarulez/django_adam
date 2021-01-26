from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, PostImage
from django import forms
from multiupload.fields import MultiFileField, MultiMediaField, MultiImageField

def index(request):
    posts = Post.objects.all()
    results = []
    for post in posts:
        obj = {
            "post": post,
            "photos": PostImage.objects.filter(post=post)
        }
        results.append(obj)
    return render(request, 'index.html', {"to_render": results} )
