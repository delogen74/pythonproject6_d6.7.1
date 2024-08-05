from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm

@login_required
def home(request):
    posts = Post.objects.all().order_by('-dateCreation')[:5]
    return render(request, 'newsapp/home.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'newsapp/news_detail.html', {'post': post})

def news_list(request):
    posts = Post.objects.all().order_by('-dateCreation')
    return render(request, 'newsapp/news_list.html', {'posts': posts})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('news_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'newsapp/create_post.html', {'form': form})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('news_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'newsapp/news_detail.html', {'post': post, 'comment_form': comment_form})

def home(request):
    posts = Post.objects.all().order_by('-dateCreation')[:5]
    return render(request, 'newsapp/home.html', {'posts': posts})

def contacts(request):
    return render(request, 'newsapp/contacts.html')

def main_info(request):
    return render(request, 'newsapp/main_info.html')