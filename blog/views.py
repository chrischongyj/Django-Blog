from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'chris',
        'title': 'first blog post',
        'content': 'hihhihi this is our first blog content',
        'date': 'August 27, 2018'
    },
    {
        'author': 'john',
        'title': 'second blog post',
        'content': 'hihhihi this is our second blog content',
        'date': 'August 28, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
