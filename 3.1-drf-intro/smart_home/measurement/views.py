# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.views import APIView
from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, OneSensorSerializer, SensorSerializer


class SensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class OneSensorView(RetrieveUpdateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return SensorSerializer
        else:
            return OneSensorSerializer

    def get_queryset(self):
        return Sensor.objects.filter(id=self.kwargs['pk'])

    
class MeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer