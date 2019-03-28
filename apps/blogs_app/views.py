from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
  # the index function is called when root is visited
def index(request):
	context = {
		"email" : "blog@gmail.com",
		"name" : "mike"
	}
	return render(request, "blogs_app/index.html", context)
def new(request):
	response = "placeholder to display a new form to crate a new blog"
	return HttpResponse(response)
def create(request):
	return redirect("/blogs")
def show(request, number):
	response = "placeohder to display blog number. For example /blogs/",number," should display a message 'placeholder to display blog",number
	return HttpResponse(response)
def edit(request, number):
	response = "placeholder to edit blog number"
	return HttpResponse(response)
def delete(request, number):
	pass
def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = "test"  # more on session below
		print "*"*50
		return redirect("/blogs")
	else:
		return redirect("/blogs")

# url(r'^blogs$', views.index),     # This line has changed!
# url(r'^blogs/new$', views.test),
# url(r'^blogs/create$', views.index), 
# url(r'^blogs/{{number}}$', views.index), 
# url(r'^blogs/{{number}}/edit$', views.index), 
# url(r'^blogs//{{number}}/delete$', views.index), 