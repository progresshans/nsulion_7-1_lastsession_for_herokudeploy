from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

def index(request):
    post_list = Post.objects
    return render(request, 'index.html', {'post_list' : post_list})

# Creat
def new(request):
    return render(request, 'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.content = request.GET['content']   
    post.user = request.user
    post.save()

    return redirect('/post/')

# Read
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post' : post_detail})

# Update
def updateForm(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if(request.user != post.user):
        return redirect('/post')
    
    return render(request, 'updateForm.html', {'post' : post})

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.title = request.GET['title']
    post.content = request.GET['content']
    post.save()
    return redirect('/post/')

# Delete
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if(request.user != post.user):
        return redirect('/post')

    post.delete()
    return redirect('/post/')