from django.urls import path
from arabapp import views

urlpatterns = [
    path('index_page/',views.index_page,name="index_page"),
    path('category_page/',views.category_page,name="category_page"),
    path('save_categories/',views.save_categories,name="save_categories"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:pid>/',views.edit_product,name="edit_product"),
    path('update_product/<int:pid>/',views.update_product,name="update_product"),
    path('delete_product/<int:pid>/', views.delete_product, name="delete_product"),
    path('add_products/',views.product_page,name="add_products"),
    path('save_products/',views.save_products,name="save_products"),
    path('product_display/', views.product_display, name="product_display"),
    path('product_edit/<int:pid>/',views.product_edit,name="product_edit"),
    path('contact_details/', views.contact_details, name="contact_details"),
    path('product_edit/<int:pid>/',views.product_edit,name="product_edit"),


]