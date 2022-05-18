from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('add-order', views.add_order, name='add-order'),
    path('show-all-orders', views.show_all_orders, name='show-all-orders'),
    path('edit-order/<int:id>', views.edit_order, name='edit-order'),
    path('delete-order/<int:id>', views.delete_order, name='edit-order'),
]
