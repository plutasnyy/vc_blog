from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.template import Context, Template

from main.models import Post as PostModel
from main.models import ImageModel

def homepage(request):
    Posts = PostModel.objects.all()
    Posts = sorted(Posts, key=lambda x: x.created_time, reverse=True)

    return render(request, 'index.html', {
        'posts': Posts
    })

class Post_Page(DetailView):
    model = PostModel
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = ImageModel.objects.all()
        rendered = Template(self.object.body).render(Context(context))
        context['post'] = self.object
        context['rendered_post'] = rendered
        return context
