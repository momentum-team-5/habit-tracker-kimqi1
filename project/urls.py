"""project URL Configuration

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
from django.conf import settings
from django.urls import include, path
from core import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" ,views.habit_list, name='habit_list'),
    path("habits/<int:pk>/", views.habit_detail, name='habit_detail'),
    path("habits/create/", views.add_habit, name='add_habit'),
    path("habits/<int:pk>/delete/", views.delete_habit, name='delete_habit'),
    path("habits/<int:pk>/update/", views.update_habit, name='update_habit'),
   # path("habits/<int:habit_pk>/records/", views.records_list, name='records_list'),
   # path("habits/<int:habit-pk>/add-record", views.add_record, name='add_record'),
#    path("records/<int:pk>/update", views.update_record, name='update_record'),
#   path("records/<int:pk>/delete/", views.delete_record, name='delete_record'),
    
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
