from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Django Ecommerce App'

urlpatterns = [

    path('admin/', admin.site.urls),

    path("demo/", include("demo.urls")),

    path("store/", include("store.urls"))
]