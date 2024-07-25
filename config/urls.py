"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import product_aggregation, customer_aggregation, order_aggregation, product_annotation, customer_annotation
from config import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('app/', include('app.urls')),
                  path('customer/', include('customer.urls')),
                  path('social-auth/',
                  path('product-aggregation/', product_aggregation, name='product-aggregation'),
                  path('customer-aggregation/', customer_aggregation, name='customer-aggregation'),
                  path('order-aggregation/', order_aggregation, name='order-aggregation'),
                  path('product-annotation/', product_annotation, name='product-annotation'),
                  path('customer-annotation/', customer_annotation, name='customer-annotation'),
                       include('social_django.urls', namespace='social')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
