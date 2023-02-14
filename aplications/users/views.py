from django.views.generic import ListView, TemplateView
from aplications.users.models import Person
from aplications.users.serializer import PersonSerializer

## django rest framework ##
from rest_framework.generics import ListAPIView
## django rest framework ##

class PersonListView(ListView):
    template_name = "users/persons_list.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        return Person.objects.all()

class ListaPersonasView(TemplateView):
    template_name = 'users/lista_personas.html'