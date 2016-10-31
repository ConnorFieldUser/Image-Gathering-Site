# from django.shortcuts import render
from django.contrib.auth.models import User

from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView


from django.views.generic import ListView
from django.urls import reverse_lazy

from image_gallery.models import Image

# Create your views here.


class IndexView(TemplateView):
        template_name = 'index.html'


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ImageListView(ListView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    fields = ('title', 'description', 'picture', 'private')
    success_url = reverse_lazy("image_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)


class ImageUpdateView(UpdateView):
    model = Image
    fields = ('title', 'description', 'picture', 'private')
    success_url = "/"
