from rest_framework import viewsets
from .models import Person, Team
from .serializers import PersonSerializer, TeamSerializer


# ViewSet for Team
class TeamListApiView(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# ViewSet for People
class PersonListApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
