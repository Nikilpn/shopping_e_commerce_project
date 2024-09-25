from django.urls import path
from webapp import views
urlpatterns=[
    path('',views.home_page,name="home"),
    path('blog_page/', views.blog_page, name="blog_page"),
    path('contact_page/', views.contact_page, name="contact_page"),


    path('our_products/', views.our_products, name="our_products"),

    path('save_contact/', views.save_contact, name="save_contact"),

    path('product_filtered/<cat_name>/', views.product_filtered, name="product_filtered"),

    path('single_products/<int:pro_id>', views.single_products, name="single_products"),
#registration _page
    path('registration_page/', views.registration_page, name="registration_page"),
    path('save_registration_page/', views.save_registration_page, name="save_registration_page"),

    path('User_login/', views.User_login, name="User_login"),

    path('user_logout/', views.user_logout, name="user_logout"),

    path('save_cart/', views.save_cart, name="save_cart"),

    path('cart_page/', views.cart_page, name="cart_page"),

    path('delete_item/<int:p_id>/', views.delete_item, name="delete_item"),
    path('user_login_page/', views.user_login_page, name="user_login_page"),

    path('checkout_page/', views.checkout_page, name="checkout_page"),
    path('save_billingaddress/', views.save_billingaddress, name="save_billingaddress"),

    path('paymentpage/', views.paymentpage, name="paymentpage"),
]