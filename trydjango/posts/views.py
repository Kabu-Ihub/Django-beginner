from django.contrib import messages
from django.shortcuts import render ,get_object_or_404,redirect
from .forms import PostForm
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from .models import Posts

def post_create(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    instance1 = form.save(commit=False)
    instance1.save()
    # return HttpResponseRedirect(instance1.get_absolute_url())
    messages.success(request,"item saved")
  else:
    messages.error(request,"Item not saved")
  context ={
    "form":form, 
  }
  return render(request,"postCreate.html" ,context)
def post_home(request):
  return HttpResponse("Hello world")

def my_name(request):
  if request.user.is_authenticated():
    context ={
      "title" :"john warui",
    }
  else:
    context ={
      "title" :"my friends",
    }

  # return render(request,"index.html" ,context)
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

def web(request):
  query = Posts.objects.all()
  paginator = Paginator(query, 5) # Show 25 contacts per page
  page = request.GET.get('page')
  query = paginator.get_page(page)

  context ={
    "Qu" :query,
    "title" : "myApp"
    
  }
  
  return render(request,"index.html" ,context)

def post_detail(request,id = None):
  postdetail = get_object_or_404(Posts,id = id)
  context={
    "title":postdetail.title,
    "instance":postdetail,
  }
  return render(request,"webindex.html" ,context)

def post_update(request,id=None):
  instance = get_object_or_404(Posts,id=id)
  form = PostForm(request.POST or None,instance=instance)
  if form.is_valid():
    instance  = form.save(commit=False)
    instance.save()
    messages.error(request,"item updated")
    return HttpResponseRedirect(instance.get_absolute_url())
  else:
    messages.warning(request,"item not updated")
  context={
    "title":instance.title,
    "instance2":instance,
    "form":form,
  }
  return render(request,"postCreate.html" ,context)

def post_delete(request,id=None):
  instance = get_object_or_404(Posts,id =id)
  instance.delete()
  messages.success(request,"Successfully deleted")
  return redirect("posts:try")

  

 
