from books.models import Book
from django.shortcuts import render
from django.views import View


# Create your views here.

class Home(View):

    def get(self, request):
        return render(request, 'home.html')


class ViewBook(View):

    def get(self, request):
        books = Book.objects.all()
        context = {'books': books}
        return render(request, viewbook.html, context)

class AddBook(View):

    def get(self, request):
        return render(request, 'addbook.html')

    def post(self, request):
        data = request.POST
        t=data['title']
        a=data['author']
        pr=data['price']
        l=data['language']
        pa=data['pages']

