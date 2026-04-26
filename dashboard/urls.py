from django.urls import path
from . import views

urlpatterns = [
    # API endpoints
    path('details/', views.detail_list),
    path('detail/<int:pk>/', views.detail_detail),
    path('create-detail/', views.create_detail),
    # Template pages
    path('details-page/', views.detail_list_page, name='detail_list_page'),
    path('create-detail-page/', views.create_detail_page, name='create_detail_page'),
]

