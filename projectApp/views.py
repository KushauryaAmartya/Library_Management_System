from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Book
from projectApp import views

# Create your views here.

def home(request):
    return render(request,"home.html")

def add(request):
    # import ipdb; ipdb.set_trace()
    if request.method=="POST":
        
        tit=request.POST['title']
        aut=request.POST['author']
        isb=request.POST['isbn']
        publi=request.POST['publicationyear']
        gen=request.POST['genre']

        
        book=Book()
        book.title=tit
        book.author=aut
        book.isbn=isb
        book.publicationyear=publi
        book.genre=gen
        book.save()
        return HttpResponse('Added Successfully')    
    return render(request,"add.html")
        

def display(request):
    books=Book.objects.all()
    return render(request,"display.html",{"books":books})

def edit(request, bookid):
    try:
        book = Book.objects.get(isbn=bookid)
        if request.method == "POST":
            # Update book details based on the form data
            book.title = request.POST['title']
            book.author = request.POST['author']
            
            book.publicationyear = request.POST['publicationyear']
            book.genre = request.POST['genre']
            book.save()
            return HttpResponse('Edited Successfully')

        return render(request, 'edit.html', {'book': book})
    except Book.DoesNotExist:
        # Handle the case where the book with the given ISBN doesn't exist.
        return HttpResponse('Book not found')

def delete(request):
    book_id = request.GET.get('bookid', None)
    if book_id is not None:
        try:
            book = Book.objects.get(isbn=book_id)
            book.delete()
        except Book.DoesNotExist:
            # Handle the case where the book with the given ISBN doesn't exist.
            pass
    return redirect('home')
