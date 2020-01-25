from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.views.generic.list import ListView, View
from .models import *
from .utils import ObjectDetailMixin
from django.template import loader
from django.http import JsonResponse
from django.db.models import Q
from main.models import Logo

def index(request):
    logo = Logo.objects.latest('pk')
    search_query = request.GET.get('search', '')

    if search_query:
        search_query = search_query.lower()
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query) |
                                    Q(title__icontains=search_query.title()) | Q(body__icontains=search_query.title()) |
                                    Q(title__icontains=search_query.upper()) | Q(body__icontains=search_query.upper()))

    else:
        posts = Post.objects.all().order_by('-pk')[:6]


    tags = Tag.objects.all().order_by('-pk')
    return render(request, 'news/news.html', {'posts': posts,
                                              'tags': tags,
                                              'search': search_query,
                                              'logo': logo})


def lazy_load_posts(request):
    print(request.POST)
    page = request.POST.get('page')
    posts = Post.objects.all().order_by('-pk')[6:]

    # use Django's pagination
    # https://docs.djangoproject.com/en/dev/topics/pagination/
    results_per_page = 6
    paginator = Paginator(posts, results_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(2)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # build a html posts list with the paginated posts
    print(posts.object_list)
    posts_html = loader.render_to_string('news/posts.html', {'posts': posts})

    # package output data and return it as a JSON object
    output_data = {'posts_html': posts_html, 'has_next': posts.has_next()}


    return JsonResponse(output_data)


class PostBody(ObjectDetailMixin,View):
    model = Post
    template = 'news/news-detail.html'

class TagDetail(ObjectDetailMixin,View):
    model = Tag
    template = 'news/tag_detail.html'
