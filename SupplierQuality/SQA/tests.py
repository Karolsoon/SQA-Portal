from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from django.utils import timezone
import datetime

from SQA.views import (SQAIndexView, SupplierListView, SupplierDetailView, PartListView, PartDetailView,
                    ClaimListView, ClaimDetailView, PPAPListView, PPAPDetailView)
from SQA.models import Supplier_T1, Subassembly, Part, PPAP, Claim, User


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

    def test_ppap_list_url_is_resolved(self):
        url = reverse('SQA:ppap_list')
        self.assertEquals(resolve(url).func.view_class, PPAPListView)   

    def test_ppap_detail_url_is_resolved(self):
        url = reverse('SQA:ppap_detail', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PPAPDetailView)  


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_date = datetime.datetime(2020, 10, 12, 8, 0, 0, 0)

        self.index_url = reverse('SQA:index')
        self.supplier_list_url = reverse('SQA:supplier_list')
        self.supplier_detail_url = reverse('SQA:supplier_detail', args=['1'])
        self.supplier_detail_url_404 = reverse('SQA:supplier_detail', args=['5'])
        self.ppap_list_url = reverse('SQA:ppap_list')
        self.ppap_detail_url = reverse('SQA:ppap_detail', args=['1'])
        self.ppap_detail_url_404 = reverse('SQA:ppap_detail', args=['5'])
        self.part_list_url = reverse('SQA:part_list')
        self.part_detail_url = reverse('SQA:part_detail', args=['1'])
        self.part_detail_url_404 = reverse('SQA:part_detail', args=['5'])
        self.claim_list_url = reverse('SQA:claim_list')
        self.claim_detail_url = reverse('SQA:claim_detail', args=['1'])
        self.claim_detail_url_404 = reverse('SQA:claim_detail', args=['5'])
        
        self.test_supplier = Supplier_T1.objects.create(
            name='Test_supplier',
            valid_from=self.test_date,
            is_9001=True,
            is_17494=True,
            id=1
        )
        self.test_part = Part.objects.create(
            part_name='Test_part',
            part_number='test_number',
            supplier_t1=self.test_supplier,
            is_produced=False,
            id=1
        )
        self.test_user = User.objects.create(
            username='Bobek'
        )
        self.test_ppap = PPAP.objects.create(
            number='test PPAP',
            part_id=self.test_part,
            quantity=1,
            revision='A',
            validated=True,
            valid_from=self.test_date,
            is_valid=True,
            id=1
        )
        self.test_claim = Claim.objects.create(
            number='8D XX-Test',
            part_id=self.test_part,
            supplier_number='test claim',
            quantity=10,
            created=self.test_date,
            created_by=self.test_user,
            closed=False,
            closed_on=None,
            supplier_t1=self.test_supplier,
            id=1,
            D3_open=False,
            D3_closed_on=timezone.now(),
            D3_on_time=True,
            D6_open=False,
            D6_closed_on=timezone.now(),
            D6_on_time=True,
            D8_open=False,
            D8_closed_on=timezone.now(),
            D8_on_time=True
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
        response = self.client.get(self.supplier_detail_url_404)

        self.assertEquals(response.status_code, 404)

    def test_ppap_list_GET(self):
        response = self.client.get(self.ppap_list_url)

        self.assertEquals(response.status_code, 200)

    def test_ppap_detail_GET(self):
        response = self.client.get(self.ppap_detail_url)

        self.assertEquals(response.status_code, 200)

    def test_ppap_detail_GET_404(self):
        response = self.client.get(self.ppap_detail_url_404)

        self.assertEquals(response.status_code, 404)

    def test_claim_list(self):
        response = self.client.get(self.claim_list_url)

        self.assertEquals(response.status_code, 200)

    def test_claim_detail_GET(self):
        response = self.client.get(self.claim_detail_url)

        self.assertEquals(response.status_code, 200)

    def test_claim_detail_GET_404(self):
        response = self.client.get(self.claim_detail_url_404)

        self.assertEquals(response.status_code, 404)


    class TestModels(TestCase):

        def setUp(self):
            pass
        