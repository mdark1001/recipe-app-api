"""
@author: Miguel Cabrera R. <miguel.cabrera@oohel.net>
@date: 03/11/21
@name: survey
"""
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from survey.models.survey import Survey

from survey.serializers import SurveyModelSerializer


class SurveyViewSets(ModelViewSet):
    """Create views for survey models  """
    # "queryset = Survey.objects.all()
    serializer_class = SurveyModelSerializer
    permission_classes = [IsAuthenticated]
    # filters
    # Motores de filtrado y ordenamiento
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend,)
    search_filters = ('name',)
    ordering = ('-created',)
    filter_fields = ('is_active',)

    def get_queryset(self):
        queryset = Survey.objects.all()
        if self.action == 'list':
            return queryset.filter(owner=self.request.user)
        return queryset

    def create(self, request):
        s = self.serializer_class(data=request.data)
        s.is_valid(raise_exception=True)
        s.save()
        return Response(s.data, status.HTTP_201_CREATED)
