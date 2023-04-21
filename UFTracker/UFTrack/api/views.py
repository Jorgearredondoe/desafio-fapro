from datetime import datetime
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError

from UFTrack.models import UF
from UFTrack.api.serializers import UFSerializer, UFDetailSerializer
from UFTrack.scrapper.scrapper import Update_DB
from UFTrack.locales.messages import message_string


class UFView(viewsets.ReadOnlyModelViewSet):
    model = UF
    queryset = UF.objects.all().order_by('-date')
    serializer_class = UFSerializer


class UFDetailAPIView(generics.ListAPIView):
    serializer_class = UFDetailSerializer

    def get_queryset(self):
        kwarg_date = self.kwargs.get('date')
        date_object = datetime.strptime(kwarg_date, '%d-%m-%Y').date()
        year = date_object.year

        if year < 2013:
            raise ValidationError(
                message_string['Validation']['year']['error'],
                code='invalid_year')

        elements_count_by_year = UF.objects.filter(
            date__year=date_object.year).count()

        if (elements_count_by_year == 0 or
                UF.objects.filter(date=date_object).exists()):
            Update_DB(str(date_object.year))

        if not UF.objects.filter(date=date_object).exists():
            raise ValidationError(
                message_string['Validation']['uf']['not_set'],
                code='UF_not_set')

        return UF.objects.filter(date=date_object)
