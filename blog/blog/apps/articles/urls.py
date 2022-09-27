from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = '_index'),
    path('<int:article_id>/', views.detail, name = '_detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = '_leave_comment'),
]