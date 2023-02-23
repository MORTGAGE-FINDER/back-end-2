from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Loans


class LoansListView(LoginRequiredMixin, ListView):
    template_name = "loans/loans_list.html"
    model = Loans
    context_object_name = "loans"


class LoansDetailView(LoginRequiredMixin, DetailView):
    template_name = "loans/loans_detail.html"
    model = Loans


class LoansUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "loans/loans_update.html"
    model = Loans
    fields = "__all__"


class LoansCreateView(LoginRequiredMixin, CreateView):
    template_name = "loans/loans_create.html"
    model = Loans
    fields = "__all__" #["name", "rating", "reviewer"]


class LoansDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "loans/loans_delete.html"
    model = Loans
    success_url = reverse_lazy("loans_list")
