from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from .models import Claim, Supplier_T1, Part, PPAP
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView


class SQAIndexView(TemplateView):
    template_name = 'SQA/index.html'

    def get(self, request):
        query = self.get_queryset()
        return render(request, 'SQA/index.html', {
            'ppaps': query[0],
            'claims': query[1]
            })


    def get_queryset(self):
        ppaps = PPAP.objects.filter(validated=False)
        claims = Claim.objects.filter(closed=False)
        print(ppaps, claims)
        return [ppaps, claims]


class SupplierListView(ListView):
    model = Supplier_T1
    template_name = 'SQA/supplier_list.html'

    def get_context_data(self, **kwargs):
        return {'suppliers': self.get_queryset()}


class SupplierDetailView(View):
    pk_url_kwarg = 'supplier_id'

    def get(self, request, supplier_id):
        print(supplier_id)
        return render(request, 'SQA/supplier_detail.html', {
            'supplier': self.get_queryset(supplier_id=supplier_id
            ), 'parts': self.get_queryset(parts=supplier_id
            ), 'claims': self.get_queryset(claims=supplier_id)
            })

    def get_queryset(self, supplier_id=None, parts=None, claims=None):
        if supplier_id:
            return Supplier_T1.objects.get(pk=supplier_id)
        if parts:
            return Part.objects.filter(supplier_t1=parts)
        if claims:
            return Claim.objects.filter(supplier_t1=claims)

    #def get_context_data(self, **kwargs):
        """
        A DetailView can return ONLY ONE queryset
        Returned queryset can be accessed by "object" in HTML template
        The returned queryset contains data relevant only to pk
        pk is passed as "supplier.id" in the supplier_list.html
        """
        #return super().get_context_data(**kwargs)


class PartListView(ListView):
    model = Part
    template_name = 'SQA/part_list.html'

    def get_context_data(self, **kwargs):
        return {'parts': self.get_queryset()}


class PartDetailView(DetailView):
    model = Part
    template_name = 'SQA/part_detail.html'
    pk_url_kwarg = 'part_id'


class ClaimListView(ListView):
    model = Claim
    template_name = 'SQA/claim_list.html'

    def get_context_data(self, **kwargs):
        return {'claims': self.get_queryset()}


class ClaimDetailView(DetailView):
    model = Claim
    template_name = 'SQA/claim_detail.html'
    pk_url_kwarg = 'claim_id'
