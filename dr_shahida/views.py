from django.shortcuts import render
from dr_shahida.models import BlogPost

def index(request):
    blog_posts = BlogPost.objects.all()
    diction = {'blog_posts':blog_posts[0:3]}

    return render(request, 'dr_shahida/index.html', context=diction)


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