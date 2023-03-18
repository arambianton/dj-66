from django.urls import path
from measurement.views import MeasurementView, SensorView, OneSensorView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<pk>/', OneSensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
