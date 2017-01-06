from django.shortcuts import render
from django.http import HttpResponse
from demo.models import Book

		# Create your views here.
def homepage(request):
	return render(request, 'homepage.html')


def search(request):
	errors = []
	if 'q' in request.GET:
		q = request.GET['q']
		if not q:
			errors.append('Enter a search term.')
		elif len(q) > 20:
			errors.append('please enter at most 20 characters.')
		else:
			books = Book.objects.filter(title__icontains=q)
			return render(request, 'search_results.html',{'books':books,'query':q})

	return render(request, 'homepage.html',{'errors':errors})
	

