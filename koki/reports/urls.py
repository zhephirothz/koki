from django.urls import path, reverse_lazy
from . import views

app_name='reports'
urlpatterns = [
    path('list/', views.AnalysisReportListView.as_view(), name='list'),
    path('upload/', views.AnalysisReportUploadView.as_view(), name='upload'),
    path('detail/<pk>/', views.AnalysisReportDetailView.as_view(), name='detail')
]
