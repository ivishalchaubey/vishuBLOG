from django.core import paginator
from django.http import request
from django.shortcuts import render
from blog.models import blogPostModel,useremail
from django.core.paginator import Paginator


def index(request):
    blogs = blogPostModel.objects.all().order_by('-id')
    if request.method =="GET":
        st = request.GET.get("search")
        if st!=None:
            blogs = blogPostModel.objects.filter(blog_title__icontains=st ).order_by('-id')
        else:
            pass
    paginator = Paginator(blogs,5)
    pageNumber = request.GET.get('page')
    pageObject = paginator.get_page(pageNumber)
    disc = {
        "pageObject": pageObject 
    }
    return render(request,"blog/index.html",disc )

def blog_post_view(req,id):
    post = blogPostModel.objects.get(id=id)
    return render(req,"blog/blog-post.html",{"posts":post})


def about_me(req):
    return render(req,'blog/about.html')
