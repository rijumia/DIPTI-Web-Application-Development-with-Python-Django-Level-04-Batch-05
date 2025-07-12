from django.shortcuts import render, redirect
from books.models import booksModel

def home(request):
    return render(request, 'home.html')

def bookList(request):
    books = booksModel.objects.all()

    return render(request, 'book_list.html',{'books':books})

def bookForm(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        category = request.POST.get('category')
        publish_date = request.POST.get('publishDate')
        description = request.POST.get('description')
        cover_image = request.FILES.get('cover')

        bookAdd = booksModel.objects.create(
            BookTitle = title,
            BookAuthor = author,
            BookCategory = category,
            BookPublishDate = publish_date,
            BookDescription = description,
            BookCoverPhoto = cover_image,
        )
        bookAdd.save()
        return redirect('bookList')
    return render(request, 'book_form.html',)

# def bookUpdate(request, id):
#     books= booksModel.objects.get(id=id)
#     if request.method == 'POST':
#         id = id,
#         title = request.POST.get('title')
#         author = request.POST.get('author')
#         category = request.POST.get('category')
#         publish_date = request.POST.get('publishDate')
#         description = request.POST.get('description')
#         cover_image = request.POST.get('cover')


#         bookAdd = booksModel.objects.create(
#             BookTitle = title,
#             BookAuthor = author,
#             BookCategory = category,
#             BookPublishDate = publish_date,
#             BookDescription = description,
#         )
#         bookAdd.save()
#         return redirect('bookList')
#     return render(request, 'book_update.html', {'books': books})
def bookUpdate(request, id):
    books = booksModel.objects.get(id=id)
    
    if request.method == 'POST':
        books.BookTitle = request.POST.get('title')
        books.BookAuthor = request.POST.get('author')
        books.BookCategory = request.POST.get('category')
        books.BookPublishDate = request.POST.get('publishDate')
        books.BookDescription = request.POST.get('description')
        
        if request.FILES.get('cover'):
            books.BookCoverPhoto = request.FILES.get('cover')
        
        books.save()
        return redirect('bookList')
    
    return render(request, 'book_update.html', {'books': books})


def bookDelete(request, id):
     book = booksModel.objects.get(id=id)
     book.delete()
     return redirect('bookList')

def viewBook(request, id):
    books = booksModel.objects.get(id=id)
    return render(request, 'view_book.html', {'books':books})

    
