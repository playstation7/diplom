from django.urls import path

from . import views

urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('news/<new_id>', views.new, name='new'),
    path('about/', views.about, name='about'),
    path('partner/', views.partner, name='partner'),
    path('connect/', views.connect, name='connect'),
    path('edit/<comment_id>', views.edit, name='edit'),
    path('delete/<comment_id>', views.delete, name='delete'),
    path('support/', views.support, name='support'),
    path('support/messages/', views.messages, name='messages'),
    path('partner/vacansies/', views.vacansies, name='vacansies'),
    path('partner/vacansies/<vacansia_id>', views.vacansia, name='vacansia'),


    #
]
