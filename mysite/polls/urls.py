from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),#pk means primary key
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('api/questions/', views.get_questions, name='get_questions'), #do http://127.0.0.1:8000/polls/api/questions/ to see the JSON file
    #note: line 12 code is misspeled it shouled be api/question not api/questions. hence the extra s between the URLs in line 12 and line 13 comments
    path('api/question/<int:pk>', views.update_question, name='update_question'), #do http://127.0.0.1:8000/polls/api/question/1
]