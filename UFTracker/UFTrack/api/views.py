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

    def date_format(self, kwarg_date):
        try:
            self.date_object = datetime.strptime(kwarg_date, '%d-%m-%Y').date()

        except ValueError:
            raise ValidationError(
                message_string['Validation']['date']['format_error'],
                code='invalid_date')

    def year_validation(self):
        if self.date_object.year < 2013:
            raise ValidationError(
                message_string['Validation']['year']['error'],
                code='invalid_year')

    def update_db(self):
        elements_count_by_year = UF.objects.filter(
            date__year=self.date_object.year).count()

        if (elements_count_by_year == 0 or
                UF.objects.filter(date=self.date_object).exists()):
            Update_DB(str(self.date_object.year))

    def uf_validation(self):
        if not UF.objects.filter(date=self.date_object).exists():
            raise ValidationError(
                message_string['Validation']['uf']['not_set'],
                code='UF_not_set')

    def get_queryset(self):
        kwarg_date = self.kwargs.get('date')

        self.date_format(kwarg_date)

        self.year_validation()

        self.update_db()

        self.uf_validation()

        return UF.objects.filter(date=self.date_object)
