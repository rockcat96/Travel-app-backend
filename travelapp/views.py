from .models import Countries
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CountriesSerializer

# Create your views here.
class CountriesViewSet(viewsets.ModelViewSet):
    queryset = Countries.objects.all()
    serializer_class = CountriesSerializer
    permission_classes = [permissions.AllowAny]