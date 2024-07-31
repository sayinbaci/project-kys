from django.shortcuts import render, HttpResponse, Http404, get_object_or_404,HttpResponseRedirect,redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html',{'posts':posts})

def post_details(request, id):
    post = get_object_or_404(Post,id=id)
    context = {
        'post' : post,
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
           post = form.save()
           messages.success(request,'Başarılı bir şekilde post oluştu.')
           return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html',context)

def post_update(request, id):
    if not request.user.is_authenticated:
         return Http404()
    
    post = get_object_or_404(Post,id=id)
    form = PostForm(request.POST or None, request.FILES or None,instance = post) 
    if form.is_valid():
           post = form.save()
           messages.success(request,'Başarılı bir şekilde post güncellendi.')
           return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form': form,
    }
    return render(request, 'post/form.html',context)

def post_delete(request, id):

    if not request.user.is_authenticated:
         return Http404()
    post = get_object_or_404(Post,id=id)
    post.delete()
    return redirect('post:index')