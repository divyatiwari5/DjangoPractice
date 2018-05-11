from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path: /model1/1
    path('<int:question_id>/', views.detail, name='detail'),
    #path: /model1/results
    path('<int:question_id>/results/', views.results, name='results'),
    #path: /model1/vote
    path('<int:question_id>/votes/', views.vote, name='vote')
]