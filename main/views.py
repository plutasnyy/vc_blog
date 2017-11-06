from django.shortcuts import render
from main.models import Post as PostModel

def homepage(request):
    Posts = PostModel.objects.all()
    Posts = sorted(Posts, key=lambda x: x.created_time, reverse=True)

    return render(request, 'main/index.html', {
        'posts': Posts
    })

def post(request, id):
    post = PostModel.objects.all().filter(id=id)[0]
    return render(request,'main/post.html',{
        'post':post
    })