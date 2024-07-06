from django.urls import path
from webapp import views

urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('about/',views.aboutpage,name="about"),
    path('contact/',views.contactpage,name="contact"),
    path('ourproducts/',views.ourproducts,name="ourproducts"),
    path('save_contact/',views.save_contact,name="save_contact"),
    path('filtered_products/<cat_name>/',views.filtered_products,name="filtered_products"),
    path('singleproduct/<int:proid>/', views.singleproduct, name="singleproduct"),

]