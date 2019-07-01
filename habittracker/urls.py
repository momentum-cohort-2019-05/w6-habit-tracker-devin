"""habittracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from core import views as core_views

urlpatterns = [
    path('', core_views.index, name='index'),
    path('', RedirectView.as_view(url='/index/', permanent=True)),
    path('habittracker/', core_views.HabitTrackerListView.as_view(), name='habittracker'),
    path('habittracker/<int:pk>', core_views.HabitTrackerDetailView.as_view(), name='habittracker-detail'),
    path('habittracker/create', core_views.HabitTrackerCreate.as_view(), name='habittracker-create'),
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
