from django.urls import path
from . import views

app_name = 'model1'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    #path: /model1/1
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path: /model1/1/results
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path: /model1/1/votes
    path('<int:question_id>/votes/', views.vote, name='vote')
]