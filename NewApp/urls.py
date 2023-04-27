from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('products',views.products,name='products'),
    path('single-product',views.single,name='single'),
    path('category',views.all_categories,name='all_categories'),
    path('<slug:slug>/',views.category_products,name='category_products'),
    path('detail/<slug:slug>/',views.detail_page,name='detail_page'),
    path('cart',views.cart,name='cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('form',views.registration,name='registration'),
    path('signin',views.login_page,name='login_page'),
    path('pluscart/<int:cart_id>/',views.pluscart,name='pluscart'),
    path('minuscart/<int:cart_id>/',views.minuscart,name='minuscart'),
    path('remove/<int:cart_id>/',views.remove,name='remove'),
    path('searchpage',views.searchresult,name='searchresult'),
    path('logout',views.logout_page,name='logout_page'),
     path('contact',views.contact_vie,name='contact_vie')
]