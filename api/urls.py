from rest_framework.documentation import include_docs_urls
from api import views
from django.urls import path, include
from api import views




urlpatterns = [
    path('spectacles/',views.ShowsList.as_view()),
    path('spectacles/<int:id_show>/', views.ShowsListById.as_view()),
    path('docs/',include_docs_urls(title='Reservation de spectacles')),
    path('testapi/',views.testapi, name='testapi'),
    path('films/',views.listefilms,name='liste_des_films'),
    path('api_google',views.api_google,name='api_google'),

]
