from django.urls import path

from . import views

app_name = 'ice_cream'

urlpatterns = [
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    path('new/', views.CreateView.as_view(), name='ice_cream_new'),
    path('<int:pk>/', views.increment_likes, name='increment_likes'),
    path('<str:selection>/', views.IndexView.as_view(), name='selection'),
    path('', views.IndexView.as_view(), name='index'),
]
