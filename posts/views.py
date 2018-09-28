from django.views.generic import ListView
from posts.models import Post


class HomePageView(ListView):
    model = Post
    context_object_name = 'all_posts_list'
    template_name = 'home.html'
