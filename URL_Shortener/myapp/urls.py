from . import views
from django.urls import path

urlpatterns = [
    # path('hello',views.hello_world),
    path('',views.home_page),
    path('all-analytics',views.all_analytics),
    path('<slug:short_url>',views.redirect_url)
]