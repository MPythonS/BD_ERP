from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django import forms

from .models import MyUser


# Register your models here.
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Slaptažodis',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Slaptažodžio patvirtinimas',
        widget=forms.PasswordInput
    )

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Slaptažodžiai nesutampa')
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = (
            'email',
            'password',
            'is_active',
            'is_admin',
            'is_superuser'
        )

    def clean_password(self):
        return self.initial['password']


class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'email',
        'is_active',
        'is_admin',
        'is_superuser'
    )
    list_filter = ('is_admin', 'is_active', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_admin',
                'is_superuser'
            )}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = []


admin.site.register(MyUser, MyUserAdmin)
