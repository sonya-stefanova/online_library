from django.shortcuts import render, redirect
from online_library.web.forms import ProfileCreateForm, ProfileDeleteForm, \
    EditProfileForm, BookCreateForm, BookEditForm
from online_library.web.models import Profile, Book


# Create your views here.

def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None



def show_home(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')

    books = Book.objects.all()

    context = {
        'profile': profile,
        'books': books,
    }

    return render(request, 'home-with-profile.html', context)


def create_profile(request):
    profile = Profile.objects.first()
    if profile is not None:
        return redirect('show home')

    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)
    
def profile(request):
    profile = Profile.objects.get()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)



def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'edit-profile.html', context)




def delete_profile(request):
    profile = get_profile()

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show home')

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)





def add_book(request):
    profile = Profile.objects.get()
    if request.method == 'POST':
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = BookCreateForm()

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'add-book.html', context)
def edit_book(request, pk):
    book = Book.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show home')
    else:
        form = BookEditForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit-book.html', context)
def details_book(request, pk):
    profile = get_profile()
    book = Book.objects.filter(pk=pk).get()

    if request.method == "GET":
        context = {
            "profile": profile,
            "book": book,
        }
        return render(request, "book-details.html", context)


def delete_book(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('show home')

