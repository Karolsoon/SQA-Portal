from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Supplier_T1
from django.views.generic import View, ListView, DetailView, TemplateView


class SQAIndexView(TemplateView):
    template_name = 'SQA/index.html'


class SupplierListView(ListView):
    model = Supplier_T1
    template_name = 'SQA/supplier_list.html'

    def get_context_data(self, **kwargs):
        return {'suppliers': self.get_queryset()}


class SupplierDetailView(DetailView):
    model = Supplier_T1
    temlplate_name = 'SQA/supplier_t1_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
