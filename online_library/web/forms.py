from django import forms
from django.db.models import Model
from online_library.web.models import Book, Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        profile = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name'
                }
            ),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL'
                }
            )
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'

class EditProfileForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')

class ProfileDeleteForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'image_url')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        if commit:
            Book.objects.all().delete()
            self.instance.delete()
        return self.instance



class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description'
                }
            ),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image'
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..'
                }
            )
        }

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'image', 'type')

