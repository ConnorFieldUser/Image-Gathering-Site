# from django.shortcuts import render
from django.contrib.auth.models import User

# from django.views.generic import TemplateView

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView


from django.views.generic import ListView
from django.urls import reverse_lazy

from image_gallery.models import Image, Comment

# Create your views here.


class IndexView(ListView):
    model = Image
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Image.objects.filter(created_user=self.request.user)
        else:
            return 'no images'


# class IndexView(TemplateView):
    # template_name = 'index.html'

    # def get_queryset(self):
    #     return Image.objects.all()
    #     return Image.objects.filter(created_user=self.request.user)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"


class ImageListView(ListView):
    model = Image


class ImageCreateView(CreateView):
    model = Image
    fields = ('title', 'description', 'picture', 'private', 'graphic')
    success_url = reverse_lazy("image_list_view")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_user = self.request.user
        return super().form_valid(form)


class ImageDetailView(DetailView):
    model = Image


class ImageUpdateView(UpdateView):
    model = Image
    fields = ('title', 'description', 'picture', 'private', 'graphic')
    success_url = "/"

# <a href="{% url 'comment_update_view' comment.id %}">{{ comment.text }}</a>


class CommentCreateView(CreateView):
    model = Comment
    success_url = "/"
    fields = ('text',)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.image = Image.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)
