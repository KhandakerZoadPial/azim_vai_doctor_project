from django.shortcuts import render, redirect
from dr_shahida.models import BlogPost
from .translation import my_dict
from django.utils.translation import to_locale, get_language



our_lang = ['en', 'bn']


def get_lang(request):
    if 'lang' in request.COOKIES:
        ln = request.COOKIES['lang']
        if ln in our_lang:
            pass
        else:
            return 'en'
    else:
        x = to_locale(get_language())
        x = x.split('_')[0]
        if x in our_lang:
            ln = x
        else:
            ln = 'en'
    return ln


def set_lang(request, ln):
    language = ln
    response = redirect('/')
    response.set_cookie('lang', language)
    return response


# Changing language url http://127.0.0.1:8000/set_language/bn
def index(request):
    blog_posts = BlogPost.objects.all()
    ln = get_lang(request)
    context = {
        'blog_posts': blog_posts,
        'lang': my_dict[ln]
    }

    

    return render(request, 'dr_shahida/index.html', context)


def about(request):
    diction = {}

    return render(request, 'dr_shahida/about.html', context=diction)

def service(request):
    diction = {}

    return render(request, 'dr_shahida/service.html', context=diction)

def testimonial(request):
    diction = {}

    return render(request, 'dr_shahida/testimonial.html', context=diction)


def appointment(request):
    diction = {}

    return render(request, 'dr_shahida/appointment.html', context=diction)

def contact(request):
    diction = {}

    return render(request, 'dr_shahida/contact.html', context=diction)


def blog(request):
    blog_posts = BlogPost.objects.all()
    diction = {'blog_posts':blog_posts}

    return render(request, 'dr_shahida/blog.html', context=diction)

def blogdetailview(request,post_id):
    blog_post = BlogPost.objects.get(pk=post_id)
    blog_posts = BlogPost.objects.all()
    
    diction = {'blog_post':blog_post, 'blog_posts':blog_posts[0:4]}

    return render(request, 'dr_shahida/detail.html', context=diction)