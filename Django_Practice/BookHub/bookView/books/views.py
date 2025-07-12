from django.shortcuts import render ,redirect
from books.models import bookModel

def home(req):
    return render(req, 'home.html')

def all_books(req):
    books = bookModel.objects.all()

    return render(req, 'allbook.html', {'books': books})

def add_book(req):
    books = bookModel.objects.all()
    if req.method == 'POST':
        book_name = req.POST.get('book_name')
        author_name = req.POST.get('author_name')
        book_price = req.POST.get('book_price')
        book_description = req.POST.get('book_description')
        book_image = req.FILES.get('book_image')
        
        book = bookModel(
            book_name=book_name,
            author_name=author_name,
            book_price=book_price,
            book_description=book_description,
            book_image=book_image
        )
        book.save()
        return redirect('all_books')
    return render(req, 'addbook.html', {'books': books})

def update_book(req, id):
    book = bookModel.objects.get(id=id)
    if req.method == 'POST':
        id = id
        book.book_name = req.POST.get('book_name')
        book.author_name = req.POST.get('author_name')
        book.book_price = req.POST.get('book_price')
        book.book_description = req.POST.get('book_description')
        if 'book_image' in req.FILES:
            book.book_image = req.FILES['book_image']
        book.save()
        return redirect('all_books')
    return render(req, 'updatebook.html', {'book': book})

def view_book(req, id):
    book = bookModel.objects.get(id=id)
    return render(req, 'viewbook.html', {'book': book})

def delete_book(req, id):
    book= bookModel.objects.get(id=id)
    book.delete()
    return redirect('all_books')