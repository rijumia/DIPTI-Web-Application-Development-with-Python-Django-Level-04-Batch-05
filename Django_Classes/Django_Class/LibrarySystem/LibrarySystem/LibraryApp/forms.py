from django import forms
from LibraryApp.models import BookModel, LibrarianProfileModel, StudentProfileModel

class BookModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'author', 'isbn', 'quantity']


class LibrarianProfileForm(forms.ModelForm):
    class Meta:
        model = LibrarianProfileModel
        fields = ['employee_id', 'designation', 'contact_number', 'address', 'profile_picture']

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfileModel
        fields = ['student_id', 'department', 'phone', 'address', 'profile_picture']