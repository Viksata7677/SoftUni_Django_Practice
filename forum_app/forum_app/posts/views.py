from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from forum_app.posts.forms import PersonForm, PostBaseForm, PostEditForm, PostDeleteForm, CommentFormSet
from forum_app.posts.models import Post


# Create your views here.


def index(request):

    form = PersonForm(request.POST or None)

    if request.method == "POST":
        print(request.POST['person_name'])

        if form.is_valid():
            print(form.cleaned_data['person_name'])

    context = {
        'my_form': PersonForm(),
    }

    return render(request, 'common/index.html', context=context)


def dashboard(request):
    content = {
        'posts': Post.objects.all()
    }

    return render(request, 'posts/dashboard.html', content)


def add_post(request):
    form = PostBaseForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'posts/add-post.html', context)


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
