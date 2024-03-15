from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from tapls.models import Tapls

from comment.forms import CommentForm

from comment.models import Comment


class NewsListView(ListView):
    model = Tapls
    template_name = 'tapls/tepls_list.html'
    context_object_name = 'tapls_list'


def tapls_detail_view(request, pk):
    object_list = Tapls.objects.filter(pk=pk)
    pk = get_object_or_404(Tapls, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            new_comment = Comment(text=text)
            new_comment.save()
            return redirect(reverse('tapls:details', kwargs={'pk': pk.pk}))

    else:
        form = CommentForm()
    return render(request, "tapls/tapls_details.html", {'form': form, 'object_list': object_list, 'pk': pk})