from django.urls import path, reverse_lazy
from . import views

app_name='reports'
urlpatterns = [
    path('list/', views.AnalysisReportListView.as_view(), name='list'),
    path('upload/', views.AnalysisReportUploadView.as_view(), name='upload'),
    path('detail/<pk>/', views.AnalysisReportDetailView.as_view(), name='detail')
    # path('customer/<int:pk>', views.CustomerDetailView.as_view(), name='customer_detail'),
    # path('customer/create',
        # views.CustomerCreateView.as_view(success_url=reverse_lazy('customers:all')), name='customer_create'),
    # path('customer/<int:pk>/update',
        # views.CustomerUpdateView.as_view(success_url=reverse_lazy('customers:all')), name='customer_update'),
    # path('customer/<int:pk>/delete',
        # views.CustomerDeleteView.as_view(success_url=reverse_lazy('customers:all')), name='customer_delete'),
    # path('customer_picture/<int:pk>', views.stream_file, name='customer_picture'),
]
