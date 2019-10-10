from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from .models import IceCream

def is_superuser_check(user):
    return user.is_superuser

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'ice_cream/index.html'

    def get_queryset(self):
        if 'selection' in self.kwargs:
            return IceCream.objects.filter(available = self.kwargs['selection'].upper())
        return IceCream.objects.all()

class CreateView(UserPassesTestMixin, generic.CreateView):
    model = IceCream
    template_name = 'ice_cream/ice_cream_new.html'
    fields = '__all__'

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('ice_cream:index')

@user_passes_test(is_superuser_check)
def delete_view(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.delete()
    return HttpResponseRedirect(reverse_lazy('ice_cream:index'))

def increment_likes(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    ice_cream.likes += 1
    ice_cream.save()
    return HttpResponseRedirect(reverse('ice_cream:index'))
