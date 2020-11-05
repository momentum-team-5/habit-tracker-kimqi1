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

urlpatterns = [
    path('admin/', admin.site.urls),
    path("habits/ ,"", habits_views.habits_list, name='habits_list'),
    path("habits/<int:pk>/", habits_views.habits_detail, name='habits_detail'),
    path("habits/create/", habits_views.add_habit, name='add_habit'),
    path("habits/<int:pk>/delete/", habits_views.delete_habit, name='delete_habit'),
    path("habits/<int:pk>/update/", habits_views.update_record, name='update_habit'),)
    path("habits/<int:habit_pk>/records/", records_views.records_list, name='records_list'),
    path("habits/<int:habit-pk>/add-record", records_views.add_record, name='add_record'),)
    path("records/<int:pk>/update", records_views.update_record, name='update_record'),
    path("records/<int:pk>/delete/", records_views.delete_record, name='delete_record'),
    
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
