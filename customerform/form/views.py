from django.shortcuts import render,redirect
from .forms import BlogForm
from .models import BlogData,CommentSection
from django.contrib.auth.decorators import login_required
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
#Function Based Views
@login_required
def BlogPost(request):
	form = BlogForm()
	if request.method == 'POST':
		form = BlogForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('BlogView')
	else:
		return render(request,'form/AddPost.html',{'form':form})

@login_required
def BlogView(request):

	if request.method == 'POST':
		# Blogid = request.POST.get('blog_id',"")
		Comment = request.POST.get('Comment',"")
		CommentSec = CommentSection(Blogid=Blogid,Comment=Comment)
		CommentSec.save()
		return redirect('BlogView')

	Blog_Objects = BlogData.objects.all()

	post_name = request.GET.get('blog_name')
	if post_name != '' and post_name is not None:
		Blog_Objects = Blog_Objects.filter(Title__icontains=post_name)

	return render(request,'form/ViewPost.html',{ 'Blog_Objects' : Blog_Objects })

@login_required
def BlogDetailView(request,id):
	Blog_Object = BlogData.objects.get(id=id)
	return render(request,'form/ViewPostDetail.html',{ 'Blog_Object' : Blog_Object })

@login_required
def BlogUpdateView(request,id):
	Blog_Object = BlogData.objects.get(id=id)
	form = BlogForm(instance = Blog_Object)
	if request.method == 'POST':
		form = BlogForm(request.POST,request.FILES,instance = Blog_Object)
		if form.is_valid():
			form.save()
			return redirect('BlogView')
	else:
		return render(request,'form/AddPost.html',{ 'form' : form })

#Class Based Views
class BlogPostClass(CreateView):
	model = BlogData
	template_name = 'form/AddPost.html'
	form_class = BlogForm

class BlogUpdateClass(UpdateView):
	model = BlogData
	template_name = 'form/AddPost.html'
	form_class = BlogForm