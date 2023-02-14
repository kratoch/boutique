from django.urls import path
from aplications.users.views import PersonListView, PersonListApiView, ListaPersonasView

app_name = 'users_app'
urlpatterns = [
    path('usuarios', PersonListView.as_view(), name='persons_list'),
    path('usuarios/lista_personas', ListaPersonasView.as_view(), name='lista_personas'),
    path('api/usuarios/list', PersonListApiView.as_view()),
]