from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views_token import TokenFormView

urlpatterns = [
    path('products/', views.product_list),
    path('product-detail/<int:pk>/', views.product_detail),
    path('create-product/', views.create_product),
    path('create-product-form/', views.create_product_form),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/form/', TokenFormView.as_view(), name='token_form'),
]
