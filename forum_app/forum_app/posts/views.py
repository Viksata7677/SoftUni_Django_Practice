from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, RedirectView, ListView, FormView, CreateView

from forum_app.posts.forms import PersonForm, PostBaseForm, PostEditForm, PostDeleteForm, CommentFormSet
from forum_app.posts.models import Post


# Create your views here.

class IndexView(TemplateView):
    template_name = 'common/index.html'  # static way

    extra_context = {
        'static_time': datetime.now()
    }  # static way

    def get_template_names(self):  # dynamic way
        if self.request.user.is_authenticated:
            return ['common/logged.html']
        else:
            return ['common/index.html']

    def get_context_data(self, **kwargs):  # dynamic way
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()

        return context

# def index(request):
#
#     form = PersonForm(request.POST or None)
#
#     if request.method == "POST":
#         print(request.POST['person_name'])
#
#         if form.is_valid():
#             print(form.cleaned_data['person_name'])
#
#     context = {
#         'my_form': PersonForm(),
#     }
#
#     return render(request, 'common/index.html', context=context)


class DashboardView(ListView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'

# FBV
# def dashboard(request):
#     content = {
#         'posts': Post.objects.all()
#     }
#
#     return render(request, 'posts/dashboard.html', content)
#
#


class AddPostView(CreateView):
    model = Post
    form_class = PostBaseForm
    template_name = 'posts/add-post.html'
    success_url = reverse_lazy('dashboard')


#
# def add_post(request):
#     form = PostBaseForm(request.POST or None, request.FILES or None)
#
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#
#     context = {
#         'form': form
#     }
#
#     return render(request, 'posts/add-post.html', context)


def edit_post(request, pk: int):
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostEditForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PostEditForm(instance=post)

    context = {
        'form': form,
        'post': post
    }

    return render(request, 'posts/edit-post.html', context)


def details_page(request, pk:int):
    post = Post.objects.get(pk=pk)
    formset = CommentFormSet(request.POST)

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.save()

            return redirect('dashboard')
    context = {
        'post': post,
        'formset': formset
    }

    return render(request, 'posts/details-page.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = PostDeleteForm(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('dashboard')

    context = {
        'post': post,
        'form': form
    }

    return render(request, 'posts/delete-post.html', context)


class MyRedirectHomeView(RedirectView):
    url = reverse_lazy('homepage')  # static way

    # def get_redirect_url(self, *args, **kwargs):  # dynamic way
    #     pass