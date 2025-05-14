from django.urls import path

from .views import (advanced_forms, buttons, dashboard1, forms, invoice,
                    modals, order_template, tables)

urlpatterns = [
	path('advanced', advanced_forms, name='advanced_forms'),
	path('forms', forms, name='forms'),
	path('button', buttons, name='buttons'),
	path('modals', modals, name='modals'),
	path('invoice', invoice, name='invoice'),
	path('tables/', tables, name='tables'),
	path('dashboard1', dashboard1, name='dashboard1'),
	path('order', order_template, name='order_form'),
]
