"""SupplierQuality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

app_name = 'SQA'
urlpatterns = [
    path('', views.SQAIndexView.as_view(), name='index'),
    path('suppliers/', include([
        path('', views.SupplierListView.as_view(), name='supplier_list'),
        path('<int:supplier_id>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    ])),
    path('parts/', include([
        path('', views.PartListView.as_view(), name='part_list'),
        path('<int:part_id>', views.PartDetailView.as_view(), name="part_detail")
    ])),
    path('claims/', include([
        path('', views.ClaimListView.as_view(), name='claim_list'),
        path('<int:claim_id>/', views.ClaimDetailView.as_view(), name='claim_detail')
    ]))
]
