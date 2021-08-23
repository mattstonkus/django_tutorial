from django.shortcuts import render

posts = [
    {
        'author': "Matt",
        'title': "First Post",
        'content': 'First post content',
        'date_posted': 'August 23, 2021'
    },
{
        'author': "Matt",
        'title': "Second Post",
        'content': 'Second post content',
        'date_posted': 'August 23, 2021'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
