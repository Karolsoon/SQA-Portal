from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.db.models import Count
from .models import Claim, Supplier_T1, Part, PPAP
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.http import JsonResponse
import json


class SQAIndexView(TemplateView):
    template_name = 'SQA/index.html'

    def get(self, request):
        query = self.get_queryset()


        return render(request, 'SQA/index.html', {
            'ppaps': query[0],
            'claims': query[1],
            })

    def get_queryset(self):
        ppaps = PPAP.objects.filter(validated=False)
        claims = Claim.objects.filter(closed=False)
        chart_data = Claim.objects.annotate(total=Count('supplier_t1')).order_by('supplier_t1')
        return [ppaps, claims, chart_data]


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
            'suppliers': Supplier_T1.objects.all(),
            'supplier': self.get_queryset(supplier_id=supplier_id
            ), 'parts': self.get_queryset(parts=supplier_id
            ), 'claims': self.get_queryset(claims=supplier_id
            ), 'ppaps:': self.get_queryset(ppaps=supplier_id
            )})

    def get_queryset(self, supplier_id=None, parts=None, claims=None, ppaps=None):
        if supplier_id:
            return get_object_or_404(Supplier_T1, pk=supplier_id)
        if parts:
            return Part.objects.filter(supplier_t1=parts)
        if claims:
            return Claim.objects.filter(supplier_t1=claims)
        if ppaps:
            return PPAP.objects.filter(validated=True)

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
        return {'parts': self.get_queryset().select_related() }


class PartDetailView(DetailView):
    model = Part
    template_name = 'SQA/part_detail.html'
    pk_url_kwarg = 'part_id'

    def get(self, request, part_id):
        return render(request, 'SQA/part_detail.html', {
            'ppaps': PPAP.objects.filter(part_id=part_id).all(),
            'parts': Part.objects.all(),
            'this_part': Part.objects.filter(pk=part_id)
        })


class ClaimListView(ListView):
    model = Claim
    template_name = 'SQA/claim_list.html'

    def get_context_data(self, **kwargs):
        return {'claims': self.get_queryset()}


class ClaimDetailView(DetailView):
    model = Claim
    template_name = 'SQA/claim_detail.html'
    pk_url_kwarg = 'claim_id'

    def get(self, request, claim_id):
        return render(request, 'SQA/claim_detail.html', {
            'claims': Claim.objects.all(),
            'claim': Claim.objects.filter(pk=claim_id)
        })


class PPAPListView(ListView):
    model = PPAP
    template_name = 'SQA/ppap_list.html'

    def get_context_data(self, **kwargs):
        return {'ppaps': self.get_queryset().select_related()}


class PPAPDetailView(DetailView):
    model = PPAP
    template_name = 'SQA/ppap_detail.html'
    pk_url_kwarg = 'ppap_id'


    def get(self, request, ppap_id):
        return render(request, 'SQA/ppap_detail.html', {
            'ppaps': PPAP.objects.all(),
            'ppap': PPAP.objects.filter(pk=ppap_id)
        })

# TESTING
def population_chart(request):
    supplier = []
    claim_total = []

    chart_data = Claim.objects.annotate(total=Count('supplier_t1')).order_by('supplier_t1').all()
    for dataset in chart_data:
        supplier.append(str(dataset.supplier_t1))
    
    supplier_set = set(supplier)
    for supplier_name in supplier_set:
        claim_total.append(supplier.count(supplier_name))
    supplier = list(supplier_set)
    print(supplier)
    print(claim_total)

    
    return JsonResponse(data={
        'labels': supplier,
        'data': claim_total,
    })