from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from blog.forms import PostForm
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def new(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            context = {'form': PostForm()}
            return render(request, 'blog/new.html', context = context)

        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.writer = request.user
                post.save()
            return redirect('/')
    else:
        return redirect('/error', context={'error':'Authorisation Error!'})
