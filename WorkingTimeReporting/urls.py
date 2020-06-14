"""WorkingTimeReporting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from app import views
from app import models


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'report_types', views.ReportTypesViewSet)
router.register(r'reports', views.ReportsViewSet)
router.register(r'projects', views.ProjectsViewSet)
router.register(r'notifications', views.NotificationsViewSet)
router.register(r'notification_statuses', views.NotificationStatusesViewSet)
router.register(r'notification_statuses', views.NotificationStatusesViewSet)
router.register(r'daily_summary', views.DailySummaryViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth-token/', authviews.obtain_auth_token, name='auth-token'),
    path('users/<int:pk>', views.getUserById),
    path('reports/user/<int:pk>', views.getReportByUserId),
    path('reports/date/<int:year>-<int:month>-<int:day>T<int:hour>:<int:minute>:<int:second>', views.getReportByDate),
]