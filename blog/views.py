from django.shortcuts import render
from django.core import paginator
from blog.models import Category,Post,Visitors,Management
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .forms import Category_Model_form,Post_Model_form,Management_Model_form,Visitors_Model_form
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.

def Homeview(request):
    cat = Category.objects.order_by('-id')
    post = Post.objects.order_by('-id')
    client = Visitors.objects.order_by('-id')
    team = Management.objects.order_by('-id')
    context = {
        'categories' : cat,
        'posts' : post,
        'visitors' : client,
        'managemnt' : team       
    }
    
    return render(request, 'blog/home.html',context)

def policy_view(request):
    return render(request, 'blog/policy-privacy.html')

def terms_view(request):
    return render(request, 'blog/terms.html')

@login_required
def Category_view_list(request):
    kat = Category.objects.order_by('-id')
    paginator = Paginator(kat, 5)
    page = request.GET.get('page')
    kats = paginator.get_page(page)
    context = {
        'categoryview' : kat,
        'kats' : kats
    }
    return render(request, 'blog/category.html',context)

@login_required

def Posts(request):
    post = Post.objects.order_by('-id')
    paginator = Paginator(post, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'post' : post,
        'posts' : posts
    }
    return render(request, 'blog/posts.html',context)

@login_required

def visitors(request):
    visit = Visitors.objects.order_by('-id')
    paginator = Paginator(visit, 5)
    page = request.GET.get('page')
    visits = paginator.get_page(page)
    context = {
        'visit' : visit,
        'visits' : visits
    }
    return render(request, 'blog/visitors.html',context)


@login_required
def Managements(request):
    mgmnt = Management.objects.order_by('-id')
    paginator = Paginator(mgmnt, 5)
    page = request.GET.get('page')
    mgmnts = paginator.get_page(page)
    context = {
        'mgmnt' : mgmnt,
        'mgmnts' : mgmnts
       
    }
    return render(request, 'blog/admin_page.html',context)

@login_required

def Category_update(request, pk):
    cat_id = get_object_or_404(Category, pk=pk)
    form = Category_Model_form(request.POST or None, instance=cat_id)
    if form.is_valid():
        obj = form.save(commit=False)       
        obj.save()
        messages.success(request, 'Category updated successfully.')
        return redirect('/category/')

    context = {
            'form' : form,
            'valueBtn' : 'Update',
            'title' : 'Update category'             
        }
    return render(request, 'blog/category-form.html',context)

@login_required

def Category_delete(request, pk):
    query = get_object_or_404(Category, pk=pk)
    query.delete()
    messages.success(request, 'Category Deleted successfully.')
    return redirect('/category/')   

@login_required

def Category_create(request):
    form = Category_Model_form(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)       
        obj.save()
        messages.success(request, 'Category added successfully.')
        return redirect('/category/')
    context = {
            'form' : form,
            'valueBtn' : 'Add',
            'title' : 'Create category'             
        }
    return render(request, 'blog/category-form.html',context)

@login_required

def Post_update_view(request, pk):
    post_id = get_object_or_404(Post, pk=pk)
    form = Post_Model_form(request.POST or None, request.FILES or None, instance=post_id)
    if form.is_valid():
         obj = form.save(commit=False)       
         obj.save()
         messages.success(request, 'Post updated successfully.')
         return redirect('/posts/')
    context = {
            'form' : form,
            'valueBtn' : 'Update',
            'title' : 'Update post'             
        }
    return render(request, 'blog/post-form.html',context)

@login_required

def Post_delete(request, pk):
    query = get_object_or_404(Post, pk=pk)
    query.delete()
    messages.success(request, 'Post deleted successfully.')
    return redirect('/posts/')  


@login_required

def Post_create(request):
    form = Post_Model_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)       
        obj.save()
        messages.success(request, 'Post added successfully.')
        return redirect('/posts/')
    context = {
            'form' : form,
            'valueBtn' : 'Add',
            'title' : 'Create post'             
        }
    return render(request, 'blog/post-form.html',context)

@login_required
def management_create(request):
    form = Management_Model_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)       
        obj.save()
        messages.success(request, 'Management added successfully.')
        return redirect('/admin_page/')
    context = {
            'form' : form,
            'valueBtn' : 'Add',
            'title' : 'Create admin page'             
        }
    return render(request, 'blog/admin_page-form.html',context)

@login_required

def Management_update(request, pk):
    mgmnt_id = get_object_or_404(Management, pk=pk)
    form = Management_Model_form(request.POST or None, request.FILES or None, instance=mgmnt_id)
    if form.is_valid():
         obj = form.save(commit=False)       
         obj.save()
         messages.success(request, 'management updated successfully.')
         return redirect('/admin_page/')
    context = {
            'form' : form,
            'valueBtn' : 'Update',
            'title' : 'Update Management'             
        }
    return render(request, 'blog/admin_page-form.html',context)

@login_required

def Management_delete(request, pk):
    query = get_object_or_404(Management, pk=pk)
    query.delete()
    messages.success(request, 'Management deleted successfully.')
    return redirect('/admin_page/')


def Visitors_create(request):
    form = Visitors_Model_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)       
        obj.save()
        messages.success(request, 'Your post sent.')
        return redirect('blog:visitors-create')
    context = {
            'form' : form,
            'valueBtn' : 'Add',
            'title' : 'Visitors page'             
        }
    return render(request, 'blog/visitors-form.html',context)
@login_required
def Visior_delete(request, pk):
    query = get_object_or_404(Visitors, pk=pk)
    query.delete()
    messages.success(request, 'Visitor deleted successfully.')
    return redirect('/visitors/')





    

