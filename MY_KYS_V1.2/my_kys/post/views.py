from django.shortcuts import render, HttpResponse,Http404, get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

def post_index(request):
    post_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
         post_list = post_list.filter(
              Q(title__icontains=query)|
              Q(content__contains=query)|
              Q(user__username__icontains=query)
              ).distinct()
    paginator = Paginator(post_list, 3)  # creating a paginator object
    # getting the desired page number from url
    page_number = request.GET.get('page')
    try:
        posts = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        posts = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        posts = paginator.page(paginator.num_pages)
  
  

    return render(request, 'post/index.html',{'posts':posts})

def post_details(request, slug):
    post = get_object_or_404(Post,slug=slug)

    form = CommentForm(request.POST or None) 
    if form.is_valid():
           
           comment = form.save(commit=False)
           comment.post = post
           comment.save()
           return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'post' : post,
        'form' : form,
    }
    return render(request, 'post/details.html',context)

def post_create(request):

    if not request.user.is_authenticated:
         return Http404()
         
    form = PostForm()
    context = {
        'form': form,
    }

        # if request.method == "POST":
        # # formdan gelen bilgileri kaydet
        # form = PostForm(request.POST)
        # if form.is_valid():
        #     form.save()
        # else:
        # # formu kullanıcıya göster 
        # form = PostForm() 

    form = PostForm(request.POST or None, request.FILES or None) 
    if form.is_valid():
           
           post = form.save(commit=False)
           post.user = request.user
           post.save()
           messages.success(request,'Başarılı bir şekilde post oluştu.')
           return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html',context)

def post_update(request, slug):
    if not request.user.is_authenticated:
         return Http404()
    
    post = get_object_or_404(Post,slug=slug)
    form = PostForm(request.POST or None, request.FILES or None,instance = post) 
    if form.is_valid():
           post = form.save()
           messages.success(request,'Başarılı bir şekilde post güncellendi.')
           return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html',context)

def post_delete(request, slug):

    if not request.user.is_authenticated:
         return Http404()
    post = get_object_or_404(Post,slug=slug)
    post.delete()
    return redirect('post:index')