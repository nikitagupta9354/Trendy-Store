"""Estore1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from MyApp import views
from django.urls import path,include
from . import settings

from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
path('adminpage/',views.Adminpage),

    path('',views.home),
    path('sop/<cn>/',views.cart),
    path('sop2/<b>/', views.cart2),
    path('pdetails/<num>/',views.pdetails),
path('prdetails/<num>/<s>/',views.pdetails2),
path('c/', views.Cartt),
path('checkout/<uname>/<gtot>/', views.Checkoutt),
path('select/<num>/', views.c3),

    path('login/',views.Login),
    path('signup/',views.Signup),
    path('profile/<username>/', views.ProfileView),
    path('logout/',views.logout),
    path('account/<uname>/', views.AccountView),
    path('Orders/<username>', views.ProfileOrders),
    path('adminproducts/',views.AdminProducts),
    path('Addproduct/', views.AddProduct),
    path('AdminDeliveredOrder/', views.AdminDeliveredOrder),
    path('AdminPendingOrder/', views.AdminPendingOrder),
    path('AdminCancelOrder/', views.AdminCancelOrder),
    path('ToDelivered/<order_no>/', views.DeliverOrder),
    path('editProduct/<pro_id>/', views.EditPro),
    path('deletepro/<str:pro_id>/', views.DeletePro),
    path('user_view_products/', views.user_view_products),
    path('select_address/<gtot>/', views.select_address),
    path('select_address/add_other_address/<uname>', views.add_address),
    path('cancel_order/<str:username>/<int:order>/',views.cancel_order),
path('addsingle/<num>/',views.CartEdit),
path('removesingle/<str:num>/',views.CartEdit1),
path('remove/<str:num>/',views.CartDelete),
    path('invoice/<uname>/<c>/<s>/<street>/<p>/',views.invoice),
    path('accounts/', include('django.contrib.auth.urls')),
             ]

urlpatterns=urlpatterns+staticfiles_urlpatterns()
urlpatterns = urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

