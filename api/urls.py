from django.urls import path

from api.views import CustomerRegisterView, get_customer_view, CategoryListView, events_view


urlpatterns = [
    path('customer/create/', CustomerRegisterView.as_view(), name='register'),
    path('customer/', get_customer_view, name='get_customer'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('events/', events_view, name='events'),
]
