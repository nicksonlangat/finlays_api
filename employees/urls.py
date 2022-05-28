from django.urls import path
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register(r'employees', views.EmployeeViewset)
router.register(r'divisions', views.DivisionViewset)

urlpatterns = [
     path('stats',views.StatsData.as_view(),name='stats'),
     path('payroll',views.PayrollView.as_view(),name='payroll'),
] + router.urls
