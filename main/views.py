from django.shortcuts import render
from main.models import Post as PostModel
from main.models import ImageModel
from django.contrib.staticfiles.storage import staticfiles_storage

def homepage(request):
    Posts = PostModel.objects.all()
    Posts = sorted(Posts, key=lambda x: x.created_time, reverse=True)

    return render(request, 'index.html', {
        'posts': Posts
    })

def post(request, id):
    post = PostModel.objects.all().filter(id=id)[0]
    images = ImageModel.objects.all()[0]
    return render(request,'post.html', dict(post=post, image=images))