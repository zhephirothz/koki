from django.urls import path, reverse_lazy
from . import views

app_name='standardspec'
urlpatterns = [
    path('list/', views.StandardSpecReportListView.as_view(), name='list'),
    path('upload/', views.StandardSpecReportUploadView.as_view(), name='upload'),
    path('detail/<pk>/', views.StandardSpecReportDetailView.as_view(), name='detail')
]
