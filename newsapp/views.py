from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from .models import Post, Comment, Author
from .forms import PostForm, CommentForm
from .filters import PostFilter
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin

@login_required
def profile(request):
    return render(request, 'newsapp/profile.html')

def test_group(request):
    is_author = request.user.groups.filter(name='Авторы').exists()
    return render(request, 'newsapp/test_group.html', {'is_author': is_author})


def home(request):
    posts = Post.objects.all().order_by('-dateCreation')[:5]
    return render(request, 'newsapp/home.html', {'posts': posts})

def news_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commentPost = post
            comment.commentUser = request.user
            comment.save()
            return redirect('news_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'newsapp/news_detail.html', {'post': post, 'comment_form': comment_form})


def news_list(request):
    posts = Post.objects.all().order_by('-dateCreation')
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    is_author = request.user.groups.filter(name='Авторы').exists() if request.user.is_authenticated else False

    return render(request, 'newsapp/news_list.html', {'page_obj': page_obj, 'is_author': is_author})
def search(request):
    post_filter = PostFilter(request.GET, queryset=Post.objects.all())
    paginator = Paginator(post_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'newsapp/search.html', {'filter': post_filter, 'page_obj': page_obj})

def contacts(request):
    return render(request, 'newsapp/contacts.html')

def main_info(request):
    return render(request, 'newsapp/main_info.html')

class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newsapp/post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('newsapp.add_post',)


    def test_func(self):
        return self.request.user.groups.filter(name='authors').exists()

    def form_valid(self, form):
        post = form.save(commit=False)
        try:
            post.author = Author.objects.get(authorUser=self.request.user)
        except Author.DoesNotExist:
            post.author = Author.objects.create(authorUser=self.request.user)
        post.categoryType = form.cleaned_data['categoryType']
        post.save()
        return super().form_valid(form)

    def handle_no_permission(self):
        return redirect('news_list')

class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'newsapp/post_form.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('newsapp.change_post',)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author.authorUser or self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('news_list')

class PostDeleteView(PermissionRequiredMixin, DeleteView):
    model = Post
    template_name = 'newsapp/post_confirm_delete.html'
    success_url = reverse_lazy('news_list')
    permission_required = ('newsapp.delete_post',)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author.authorUser or self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('news_list')
