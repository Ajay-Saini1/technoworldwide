from django.urls import path
from .views import *

urlpatterns = [

    path('register/', CustomerCreateView.as_view(), name='register_customer'),
    path('login/', CustomerLogin.as_view(), name='login'),
    path('website/', WebisteView.as_view(), name='website'),
    path('customer-list/', CreateCustomerView.as_view(), name='customer_list'),
    path('Customer/list/ajax', ListCustomerViewJson.as_view(), name='Customer-list-ajax'),
    path('Customer/delete/<int:pk>', DeleteCustomerView.as_view(), name='Customer-user-delete'),
    path('Customer/update/<int:pk>', CustomerUpdateView.as_view(), name='Customer-user-update'),
    path('change_customer_status/<int:pk>/<str:is_active>/', change_customer_status, name='change_customer_status'),
    # export url to
    path('export-excel/', CustomerExportView.as_view(), name='create_export_customer'),

    # customer address urls

    path('customer_address_add/', CustomerAddressCreateView.as_view(), name='add_address'),
    path('list_customers/', CustomerAddressListView.as_view(), name='customer_address_list'),
    path('Customer_address/list/ajax', ListCustomerAddressViewJson.as_view(), name='Customer-address-list-ajax'),
    path('edit/<int:pk>/', CustomerAddressUpdateView.as_view(), name='edit_address'),
    path('delete/<int:pk>/', CustomerAddressDeleteView.as_view(), name='delete_address'),

    # contact us page
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact-us-list/', ContactUsListView.as_view(), name='contact_list'),
    path('Contact-us/list/ajax', ListContactUsViewJson.as_view(), name='Contact-us-list-ajax'),

]
