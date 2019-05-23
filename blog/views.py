from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import HttpResponse
from blog.forms import PostForm
from blog.models import Post
# Create your views here.


def index(request):

    try:
        id = request.GET['id']
        return render(request, 'blog/index.html', context={'post':Post.objects.get(pk=id)})
    except MultiValueDictKeyError:
        return redirect('/')

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
                print(request.FILES)
                #post.image = request.FILES['image']
                post.save()
            return redirect('/')
    else:
        return redirect('/error', context={'error':'Authorisation Error!'})
