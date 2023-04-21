from rest_framework import serializers
from UFTrack.models import UF


class UFSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = UF
        exclude = ['id', 'created_at', 'updated_at']

    def get_value(self, instance):
        if instance.value == -1.0:
            return None
        return instance.value

    def get_date(self, instance):
        return instance.date.strftime('%d-%m-%Y')


class UFDetailSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()
    # Uncomment this line if you want to get the date of the UF
    # date = serializers.SerializerMethodField()

    class Meta:
        model = UF
        exclude = ['id', 'created_at', 'updated_at']
        # Comment this line if you want to get the date of the UF
        exclude.append('date')

    def get_value(self, instance):
        if instance.value == -1.0:
            return None
        return instance.value

    # Uncomment this line if you want to get the date of the UF
    # def get_date(self, instance):
    #     return instance.date.strftime('%d-%m-%Y')
