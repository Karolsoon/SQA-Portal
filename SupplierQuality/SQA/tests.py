from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.utils import timezone
import datetime

from SQA.views import SQAIndexView, SupplierListView, SupplierDetailView, PartListView, PartDetailView, ClaimListView, ClaimDetailView
from SQA.models import Supplier_T1, Subassembly, Part, PPAP, Claim

class TestUrls(SimpleTestCase):


    def test_index_url_is_resolved(self):
        url = reverse('SQA:index')
        self.assertEquals(resolve(url).func.view_class, SQAIndexView)
    
    def test_supplier_list_url_is_resolved(self):
        url = reverse('SQA:supplier_list')
        self.assertEquals(resolve(url).func.view_class, SupplierListView)        

    def test_supplier_detail_url_is_resolved(self):
        url = reverse('SQA:supplier_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, SupplierDetailView)    

    def test_part_list_url_is_resolved(self):
        url = reverse('SQA:part_list')
        self.assertEquals(resolve(url).func.view_class, PartListView)

    def test_part_detail_url_is_resolved(self):
        url = reverse('SQA:part_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PartDetailView)

    def test_claim_list_url_is_resolved(self):
        url = reverse('SQA:claim_list')
        self.assertEquals(resolve(url).func.view_class, ClaimListView)   

    def test_claim_detail_url_is_resolved(self):
        url = reverse('SQA:claim_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ClaimDetailView)   


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('SQA:index')
        self.supplier_list_url = reverse('SQA:supplier_list')
        self.supplier_detail_url = reverse('SQA:supplier_detail', args=['1'])
        self.supplier_detail_url2 = reverse('SQA:supplier_detail', args=['5'])
        
        self.test_supplier = Supplier_T1.objects.create(
            name='Test_supplier', valid_from=datetime.datetime(2020, 10, 12, 8, 0, 0, 0),
            is_9001=True, is_17494=True, id=1
        )
        self.test_part = Part.objects.create(
            part_name='Test_part', part_number='test_number', supplier_t1=self.test_supplier,
            is_produced=False
        )

    
    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'SQA/index.html')
    
    def test_supplier_list_GET(self):
        response = self.client.get(self.supplier_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'SQA/supplier_list.html')

    def test_supplier_detail_GET(self):
        response = self.client.get(self.supplier_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'SQA/supplier_detail.html')

    def test_supplier_detail_GET_404(self):
        response = self.client.get(self.supplier_detail_url2)

        self.assertEquals(response.status_code, 404)
