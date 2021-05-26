from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from .models import Cheese
from django.contrib.auth.mixins import LoginRequiredMixin


class CheeseListView(ListView):
    model = Cheese


class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country']

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CheeseDetailView(DetailView):
    model = Cheese
