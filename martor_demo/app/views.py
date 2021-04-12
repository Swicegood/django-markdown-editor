from django.conf import settings
from django.shortcuts import (render, redirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def home_redirect_view(request):
    return redirect('overview')


def overview_view(request):
    
    return render(request, 'overview.html')


@login_required
def post_form_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            messages.success(request, '%s successfully saved.' % post.title)
            return redirect('test_markdownify')
    else:
        form = PostForm()
        context = {'form': form, 'title': 'Post Form'}
    theme = getattr(settings, 'MARTOR_THEME', 'bootstrap')
    return render(request, '%s/form.html' % theme, context)


def test_markdownify(request):
    post = Post.objects.last()
    context = {'post': post}
    if post is None:
        context = {
            'post': {
                'title': 'Fake Post',
                'description': """It **working**! :heart: [Python Learning](https://python.web.id)"""
            }
        }
    theme = getattr(settings, 'MARTOR_THEME', 'bootstrap')
    return render(request, '%s/test_markdownify.html' % theme, context)
