from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Supplier_T1, Part, PPAP
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
    pk_url_kwarg = 'supplier_id'

    def get_context_data(self, **kwargs):
        """
        A DetailView can return ONLY ONE queryset
        Returned queryset can be accessed by "object" in HTML template
        The returned queryset contains data relevant only to pk
        pk is passed as "supplier.id" in the supplier_list.html
        """
        return super().get_context_data(**kwargs)

class PartListView(ListView):
    model = Part
    template_name = 'SQA/part_list.html'

    def get_context_data(self, **kwargs):
        return {'parts': self.get_queryset()}


# NEEDS ATTENTION
def supplier_part_list(request, supplier_id):
    parts = Part.objects.all()
    return render(request, 'SQA/supplier_part_list.html', {'parts': parts})
